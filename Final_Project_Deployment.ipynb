{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "view-in-github"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/RFOXgithub/Sistem-Rekomendasi-Pengelolaan-Produk/blob/main/Final_Project_Deployment.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 45,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7lfYHxLzNcgF",
        "outputId": "cacdb1c8-10f6-4bdd-f8b0-006ce20d11a6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import pickle\n",
        "from joblib import load\n",
        "\n",
        "# Load models\n",
        "rf_modelStock = load('rf_modelStock.joblib')\n",
        "rf_modelPrice = load('rf_modelPrice.joblib')\n",
        "with open('xgb_modelPopu.pkl', 'rb') as f:\n",
        "    xgb_modelPopu = pickle.load(f)\n",
        "\n",
        "# Define categories\n",
        "categories = [\n",
        "    'Elektronik', 'Lainnya', 'Perawatan Pribadi', 'Olahraga & Outdoor',\n",
        "    'Peralatan Rumah Tangga', 'Pakaian & Fashion', 'Kendaraan & Aksesori',\n",
        "    'Makanan & Minuman', 'Perhiasan & Aksesori', 'Mainan & Anak-Anak',\n",
        "    'Gadget & Elektronik Musik'\n",
        "]\n",
        "\n",
        "# Define prediction function\n",
        "def prediction(df):\n",
        "    df['avg_harga_per_kategori'] = df.groupby('kategori')['harga'].transform('mean')\n",
        "    df['harga_per_rating'] = df['harga'] / (df['total_rating'] + 1)\n",
        "    df['harga_terjual'] = df['harga'] * df['terjual']\n",
        "    df['rasio_penjualan_stok'] = df['terjual'] / (df['stock'] + 1)\n",
        "    df['stok_terjual_ratio'] = df['stock'] / (df['terjual'] + 1)\n",
        "    df['stok_ideal'] = np.ceil(df['stok_terjual_ratio'] * df['stock'])\n",
        "\n",
        "    df['harga_kategori_encoding'] = rf_modelPrice.predict(\n",
        "        df[['avg_harga_per_kategori', 'harga_per_rating', 'harga_terjual']]\n",
        "    )\n",
        "    df['restock_encoding'] = rf_modelStock.predict(\n",
        "        df[['stok_ideal', 'stok_terjual_ratio', 'rasio_penjualan_stok']]\n",
        "    )\n",
        "    df['popularitas_encoding'] = xgb_modelPopu.predict(\n",
        "        df[['harga_per_rating', 'rasio_penjualan_stok', 'total_rating']]\n",
        "    )\n",
        "\n",
        "    harga_kategori_mapping = {0: 'Rendah', 1: 'Sedang', 2: 'Tinggi'}\n",
        "    restock_mapping = {1: 'Tidak Restock', 2: 'Restock', 0: 'Stok Berlebih'}\n",
        "    popularitas_mapping = {0: 'Tidak Populer', 1: 'Populer', 2: 'Sangat Populer'}\n",
        "\n",
        "    df['harga_kategori'] = df['harga_kategori_encoding'].map(harga_kategori_mapping)\n",
        "    df['restock'] = df['restock_encoding'].map(restock_mapping)\n",
        "    df['popularitas'] = df['popularitas_encoding'].map(popularitas_mapping)\n",
        "\n",
        "    def rekomendasi(row):\n",
        "        if row['restock'] == 'Restock':\n",
        "            return \"Segera lakukan restock produk ini.\"\n",
        "        elif row['harga_kategori'] == 'Tinggi' and row['popularitas'] == 'Sangat Populer':\n",
        "            return \"Lakukan promosi pada produk populer ini.\"\n",
        "        elif row['restock'] == 'Tidak Restock' and row['harga_kategori'] == 'Rendah':\n",
        "            return \"Evaluasi produk untuk diskon atau hapus dari katalog.\"\n",
        "        elif row['popularitas'] == 'Tidak Populer' and row['restock'] == 'Stok Berlebih':\n",
        "            return \"Tunda restock produk ini dan evaluasi penjualannya.\"\n",
        "        elif row['popularitas'] == 'Populer' and row['harga_kategori'] == 'Sedang':\n",
        "            return \"Pertahankan produk dengan harga dan popularitas saat ini.\"\n",
        "        else:\n",
        "            return \"Pertahankan strategi saat ini.\"\n",
        "\n",
        "    df['Rekomendasi'] = df.apply(rekomendasi, axis=1)\n",
        "    return df[['nama_produk', 'harga_kategori', 'restock', 'popularitas', 'Rekomendasi']]\n",
        "\n",
        "# Define Streamlit app\n",
        "def main():\n",
        "    st.title(\"Sistem Rekomendasi Produk\")\n",
        "    st.markdown(\"\"\"\n",
        "    <div style=\"background-color:yellow;padding:13px\">\n",
        "    <h1 style=\"color:black; text-align:center;\">Aplikasi Analisis dan Rekomendasi Produk</h1>\n",
        "    </div>\n",
        "    \"\"\", unsafe_allow_html=True)\n",
        "\n",
        "    if 'hasil' not in st.session_state:\n",
        "        st.session_state['hasil'] = None\n",
        "\n",
        "    with st.form(key='my_form'):\n",
        "        nama_produk = st.text_input(\"Nama Produk\", key=\"nama_produk_key\")\n",
        "        kategori = st.selectbox(\"Pilih Kategori\", categories, key=\"kategori_key\")\n",
        "        harga = st.number_input(\"Harga\", min_value=0, step=1000, key=\"harga_key\")\n",
        "        total_rating = st.number_input(\"Total Rating\", min_value=0, step=1, key=\"rating_key\")\n",
        "        min_terjual = total_rating if total_rating > 0 else 0\n",
        "        terjual = st.number_input(\"Jumlah Terjual\", min_value=min_terjual, step=1, key=\"terjual_key\")\n",
        "        stock = st.number_input(\"Stock\", min_value=0, step=1, key=\"stock_key\")\n",
        "        submit_button = st.form_submit_button(label=\"Proses Rekomendasi\")\n",
        "\n",
        "    if submit_button:\n",
        "        kategori_index = categories.index(kategori) + 1\n",
        "        data_input = {\n",
        "            'nama_produk': [nama_produk],\n",
        "            'kategori': [kategori_index],\n",
        "            'harga': [harga],\n",
        "            'total_rating': [total_rating],\n",
        "            'terjual': [terjual],\n",
        "            'stock': [stock]\n",
        "        }\n",
        "        df = pd.DataFrame(data_input)\n",
        "        st.session_state['hasil'] = prediction(df)\n",
        "\n",
        "    if st.session_state['hasil'] is not None:\n",
        "        st.success(\"Berikut adalah hasil analisis produk:\")\n",
        "        st.dataframe(st.session_state['hasil'])\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "authorship_tag": "ABX9TyNoBBHMkmCw9yk8yAqlZoIP",
      "include_colab_link": true,
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
