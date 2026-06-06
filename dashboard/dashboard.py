import streamlit as st
import pandas as pd
import joblib
import os
import math
from datetime import datetime

# Konfigurasi halaman streamlit
st.set_page_config(page_title="PowerAnalytics", page_icon="⚡", layout="wide")

# Session state untuk menyimpan riwayat analisis
if "history" not in st.session_state:
    st.session_state.history = []


def delete_history(index):
    st.session_state.history.pop(index)


# Cache untuk memuat model
@st.cache_resource
def load_ml_components():
    MODEL_DIR = "models"
    try:
        scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
        lr_model = joblib.load(os.path.join(MODEL_DIR, "lr_model.pkl"))
        dt_model = joblib.load(os.path.join(MODEL_DIR, "dt_model.pkl"))
        target_discretizer = joblib.load(
            os.path.join(MODEL_DIR, "target_discretizer.pkl")
        )
        return scaler, lr_model, dt_model, target_discretizer
    except Exception as e:
        st.error(f"Gagal memuat komponen model. Error: {e}")
        return None, None, None, None


scaler, lr_model, dt_model, target_discretizer = load_ml_components()

# Layout sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616494.png", width=120)
    st.title("Manajemen Energi")
    st.markdown("---")

    # Menampilkan informasi batas ambang kategori
    if target_discretizer:
        edges = target_discretizer.bin_edges_[0]
        st.markdown("### 📊 Batas Kategori Konsumsi")
        st.write(f"- **Low**: < {edges[1]:,.2f} kWh")
        st.write(f"- **Medium**: {edges[1]:,.2f} - {edges[2]:,.2f} kWh")
        st.write(f"- **High**: > {edges[2]:,.2f} kWh")
    else:
        st.warning("Batas ambang kategori gagal dimuat.")

    st.markdown("---")
    st.caption(
        "Dashboard ini dibuat untuk menganalisis karakteristik fisik bangunan serta faktor "
        "lingkungan guna memprediksi nilai konsumsi energi (kWh) dan status efisiensinya."
    )

# Layout utama
st.title("PowerAnalytics: Prediksi Konsumsi Energi Gedung ⚡")
st.markdown(
    "Menampilkan insight estimasi penggunaan daya listrik dan status efisiensi operasional bangunan berdasarkan parameter teknis."
)
st.markdown("---")

tab1, tab2, tab3 = st.tabs(
    ["🔍 Prediksi Konsumsi", "📖 Panduan Parameter", "🕒 Riwayat Analisis"]
)

# Memastikan komponen model termuat
if scaler and lr_model and dt_model:
    # Tab 1 untuk prediksi konsumsi energi
    with tab1:
        with st.container(border=True):
            st.subheader("Karakteristik & Kondisi Gedung")

            col1, col2, col3 = st.columns(3)
            with col1:
                square_footage = st.slider(
                    "Luas Gedung (Square Footage)",
                    min_value=5000,
                    max_value=50000,
                    value=15000,
                    step=100,
                )
                num_occupants = st.slider(
                    "Jumlah Penghuni (Number of Occupants)",
                    min_value=10,
                    max_value=100,
                    value=40,
                    step=1,
                )
            with col2:
                appliances_used = st.slider(
                    "Peralatan Listrik (Appliances Used)",
                    min_value=5,
                    max_value=60,
                    value=25,
                    step=1,
                )
                avg_temperature = st.slider(
                    "Suhu Udara (Average Temperature)",
                    min_value=10.0,
                    max_value=40.0,
                    value=25.0,
                    step=0.5,
                )
            with col3:
                building_type = st.selectbox(
                    "Tipe Bangunan (Building Type)",
                    ["Commercial", "Industrial", "Residential"],
                )
                day_of_week = st.selectbox(
                    "Hari Operasional (Day of Week)", ["Weekday", "Weekend"]
                )

        # Pemetaan fitur kategorikal
        building_type_industrial = True if building_type == "Industrial" else False
        building_type_residential = True if building_type == "Residential" else False
        day_of_week_weekend = True if day_of_week == "Weekend" else False

        # Fitur input untuk model prediksi
        feature_names = [
            "Square Footage",
            "Number of Occupants",
            "Appliances Used",
            "Average Temperature",
            "Building Type_Industrial",
            "Building Type_Residential",
            "Day of Week_Weekend",
        ]

        input_data = [
            {
                "Square Footage": float(square_footage),
                "Number of Occupants": float(num_occupants),
                "Appliances Used": float(appliances_used),
                "Average Temperature": float(avg_temperature),
                "Building Type_Industrial": building_type_industrial,
                "Building Type_Residential": building_type_residential,
                "Day of Week_Weekend": day_of_week_weekend,
            }
        ]

        features_df = pd.DataFrame(input_data, columns=feature_names)

        # Transformasi skala kolom numerik
        numeric_cols = [
            "Square Footage",
            "Number of Occupants",
            "Appliances Used",
            "Average Temperature",
        ]
        features_scaled_df = features_df.copy()
        features_scaled_df[numeric_cols] = scaler.transform(features_df[numeric_cols])

        # Prediksi dan klasifikasi
        predicted_kwh = lr_model.predict(features_scaled_df)[0]
        predicted_class_idx = dt_model.predict(features_scaled_df)[0]

        class_mapping = {0: "LOW (Efisien)", 1: "MEDIUM (Wajar)", 2: "HIGH (Boros)"}
        status_text = class_mapping[predicted_class_idx]

        if predicted_class_idx == 0:
            status_icon = "🟢"
            alert_type = "success"
        elif predicted_class_idx == 1:
            status_icon = "🟡"
            alert_type = "warning"
        else:
            status_icon = "🔴"
            alert_type = "error"

        # Hasil analisis dan insight
        st.write("")
        st.subheader("Hasil Analisis")

        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric(
                label="Estimasi Nilai Konsumsi Energi",
                value=f"{predicted_kwh:,.2f} kWh",
            )
        with col_m2:
            if alert_type == "success":
                st.success(f"### {status_icon} STATUS: {status_text}")
            elif alert_type == "warning":
                st.warning(f"### {status_icon} STATUS: {status_text}")
            else:
                st.error(f"### {status_icon} STATUS: {status_text}")

        st.info(
            f"**💡 Insight:** Parameter pada gedung tipe **{building_type}** memicu estimasi "
            f"daya listrik akhir sebesar **{predicted_kwh:,.2f} kWh** ({status_text})."
        )

        st.markdown("---")

        # Tombol untuk menyimpan hasil prediksi ke riwayat
        if st.button(
            "💾 Simpan Hasil Prediksi",
            type="primary",
            use_container_width=True,
        ):
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            st.session_state.history.append(
                {
                    "time": timestamp,
                    "kwh": f"{predicted_kwh:,.2f} kWh",
                    "status": status_text,
                    "icon": status_icon,
                    "alert": alert_type,
                    "params": {
                        "Square Footage": square_footage,
                        "Number of Occupants": num_occupants,
                        "Appliances Used": appliances_used,
                        "Average Temperature": avg_temperature,
                        "Building Type": building_type,
                        "Day of Week": day_of_week,
                    },
                }
            )
            st.toast("Prediksi berhasil disimpan ke tab riwayat!", icon="💾")

    # Tab 2 untuk panduan parameter
    with tab2:
        st.subheader("Panduan Parameter Evaluasi")
        st.write(
            "Berikut adalah penjelasan untuk setiap elemen pengukuran karakteristik bangunan:"
        )

        with st.expander("Square Footage (Luas Gedung)"):
            st.info(
                "Total luas lantai internal bangunan keseluruhan. Semakin besar luas area bangunan, secara linier akan meningkatkan kebutuhan energi dasar untuk pencahayaan dan tata udara."
            )
        with st.expander("Number of Occupants (Jumlah Penghuni)"):
            st.info(
                "Jumlah total individu yang menempati atau beraktivitas di dalam gedung. Peningkatan jumlah manusia menambah beban panas laten dalam ruangan yang memicu sistem pendingin bekerja lebih keras."
            )
        with st.expander("Appliances Used (Peralatan Listrik)"):
            st.info(
                "Kuantitas perangkat elektronik, mesin operasional, komponen IT, atau instrumen beban kerja listrik lainnya yang aktif secara bersamaan di dalam gedung."
            )
        with st.expander("Average Temperature (Suhu Udara)"):
            st.info(
                "Suhu udara lingkungan di sekitar gedung dalam satuan Celsius (°C). Fluktuasi suhu luar berdampak langsung pada performa kompresor AC ruangan."
            )
        with st.expander("Building Type (Tipe Bangunan)"):
            st.info(
                "Fungsi operasional utama bangunan (Commercial, Industrial, Residential). Perbedaan fungsi dasar ini menentukan profil baseload energi."
            )
        with st.expander("Day of Week (Hari Operasional)"):
            st.info(
                "Klasifikasi hari pengamatan (Weekday atau Weekend). Membantu membedakan jadwal aktivitas beban puncak antara hari kerja normal dan hari libur."
            )

    # Tab 3 untuk riwayat prediksi
    with tab3:
        st.subheader("Riwayat Analisis")

        total_items = len(st.session_state.history)

        if total_items == 0:
            st.info(
                "Belum ada riwayat analisis yang disimpan. Silakan tekan tombol 'Simpan Hasil Prediksi' di tab 'Prediksi Konsumsi'."
            )
        else:
            st.write(f"Total pengujian pada sesi ini: **{total_items} data**")

        # Unduh seluruh riwayat
        if total_items > 0:
            history_df = pd.DataFrame(
                [
                    {
                        "Waktu": item["time"],
                        "Prediksi (kWh)": item["kwh"],
                        "Status Efisiensi": item["status"],
                        "Luas Gedung": item["params"]["Square Footage"],
                        "Jumlah Penghuni": item["params"]["Number of Occupants"],
                        "Peralatan Listrik": item["params"]["Appliances Used"],
                        "Suhu Udara": item["params"]["Average Temperature"],
                        "Tipe Bangunan": item["params"]["Building Type"],
                        "Hari Operasional": item["params"]["Day of Week"],
                    }
                    for item in st.session_state.history
                ]
            )

            # Mengonversi data riwayat ke format csv
            csv_data = history_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Unduh Seluruh Riwayat (CSV)",
                data=csv_data,
                file_name=f"riwayat_prediksi_energi_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True,
            )

            # Konfigurasi pembagian halaman
            ITEMS_PER_PAGE = 5
            total_pages = math.ceil(total_items / ITEMS_PER_PAGE)

            if total_pages > 1:
                current_page = st.radio(
                    "Pilih Halaman Riwayat:",
                    options=range(1, total_pages + 1),
                    horizontal=True,
                )
            else:
                current_page = 1

            start_idx = (current_page - 1) * ITEMS_PER_PAGE
            end_idx = start_idx + ITEMS_PER_PAGE

            # Render item riwayat secara berurutan sesuai halaman aktif
            for i in range(start_idx, min(end_idx, total_items)):
                record = st.session_state.history[i]

                with st.container(border=True):
                    col_text, col_btn = st.columns([5, 1])

                    with col_text:
                        st.write(f"**🕒 Waktu Penyimpanan:** {record['time']}")
                        st.write(
                            f"📊 **Hasil Prediksi:** `{record['kwh']}` | Status: {record['icon']} **{record['status']}**"
                        )

                        if "params" in record:
                            with st.expander("Lihat Rincian Parameter Input"):
                                p = record["params"]
                                c1, c2, c3 = st.columns(3)

                                with c1:
                                    st.caption(
                                        f"Luas Gedung: {p['Square Footage']:,} sqft"
                                    )
                                    st.caption(
                                        f"Jumlah Penghuni: {p['Number of Occupants']} orang"
                                    )
                                with c2:
                                    st.caption(
                                        f"Peralatan Listrik: {p['Appliances Used']} unit"
                                    )
                                    st.caption(
                                        f"Suhu Udara: {p['Average Temperature']} °C"
                                    )
                                with c3:
                                    st.caption(f"Tipe Bangunan: {p['Building Type']}")
                                    st.caption(f"Hari Operasional: {p['Day of Week']}")

                    # Tombol hapus untuk setiap item riwayat
                    with col_btn:
                        st.button(
                            "🗑️ Hapus",
                            key=f"del_energy_{i}_{record['time']}",
                            on_click=delete_history,
                            args=(i,),
                            use_container_width=True,
                        )
else:
    st.error("Gagal memuat sistem prediksi. Pastikan semua komponen model tersedia.")

# Footer
st.markdown("---")
st.caption("© 2026 Muhammad Fikri Rouzan Ash Shidik")
