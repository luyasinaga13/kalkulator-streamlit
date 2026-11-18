import streamlit as st

st.title("🧮 Kalkulator Sederhana")
st.write("Aplikasi kalkulator interaktif untuk tugas Matematika Diskrit.")

st.divider()

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Masukkan angka pertama:", value=0.0, step=1.0)
with col2:
    num2 = st.number_input("Masukkan angka kedua:", value=0.0, step=1.0)

operation = st.selectbox(
    "Pilih Operasi Matematika:",
    ["Penjumlahan (+)", "Pengurangan (-)", "Perkalian (×)", "Pembagian (÷)"]
)

if st.button("Hitung Hasil", type="primary"):
    result = None
    if operation == "Penjumlahan (+)":
        result = num1 + num2
        op = "+"
    elif operation == "Pengurangan (-)":
        result = num1 - num2
        op = "-"
    elif operation == "Perkalian (×)":
        result = num1 * num2
        op = "×"
    elif operation == "Pembagian (÷)":
        if num2 != 0:
            result = num1 / num2
            op = "÷"
        else:
            st.error("Error: Pembagian dengan angka nol tidak diperbolehkan!")

    if result is not None:
        st.success(f"**Hasil:** {num1} {op} {num2} = **{result}**")