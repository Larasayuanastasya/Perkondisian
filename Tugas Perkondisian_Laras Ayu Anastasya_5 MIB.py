{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ea28047-c082-4bf6-bcfa-b863aa389fbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def nama_fungsi():\n",
    "    print (\"Hello ini Fungsi\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "018814bf-1dbf-4fe9-8949-0a11302fe554",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Membuat Fungsi\n",
    "def salam():\n",
    "    print (\"Hello, Selamat Pagi\")\n",
    "\n",
    "## Pemanggilan Fungsi\n",
    "salam()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca2f73a9-d20b-4a24-bb99-71b61ef819cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Membuat Fungsi\n",
    "def salam():\n",
    "    print (\"Hello, Selamat Pagi\")\n",
    "\n",
    "## Pemanggilan Fungsi\n",
    "salam()\n",
    "salam()\n",
    "salam()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ec19e0e-5eaa-4f3d-ad94-b6443c2ac231",
   "metadata": {},
   "outputs": [],
   "source": [
    "def salam(ucapan):\n",
    "    print(ucapan)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1564c08f-1c34-4709-9ab1-713069f60002",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fungsi(parameter):\n",
    "    print(parameter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd9a5670-8d00-450b-8500-155b4a985776",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Membuat fungsi dengan parameter\n",
    "def luas_segitiga(alas, tinggi):\n",
    "    luas = (alas * tinggi) / 2\n",
    "    print(\"Luas segitiga: %f\" % luas)\n",
    "\n",
    "# Pemanggilan fungsi\n",
    "luas_segitiga(4, 6)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff5ec71e-f14c-41ee-b46c-71804267b782",
   "metadata": {},
   "outputs": [],
   "source": [
    "def luas_persegi(sisi):\n",
    "    luas = sisi * sisi\n",
    "    return luas\n",
    "\n",
    "# pemanggilan fungsi\n",
    "print (\"Luas persegi: %d\" % luas_persegi(6))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aecce10d-6d1c-470b-a6f2-a5a8e437b029",
   "metadata": {},
   "outputs": [],
   "source": [
    "# rumus: sisi x sisi\n",
    "def luas_persegi(sisi):\n",
    "    luas = sisi * sisi\n",
    "    return luas\n",
    "\n",
    "\n",
    "# rumus: sisi x sisi x sisi\n",
    "def volume_persegi(sisi):\n",
    "    volume = luas_persegi(sisi) * sisi\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "55dc525d-6f19-42df-892d-1bdb2e9ce169",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nama: Firmansyah\n",
      "Versi: 1.0.0\n",
      "Nama: Programku\n",
      "Versi: 1.0.2\n"
     ]
    }
   ],
   "source": [
    "# membuat variabel global\n",
    "nama = \"Laras Ayu Anastasya\"\n",
    "versi = \"1.0.0\"\n",
    "\n",
    "def help():\n",
    "    # ini variabel lokal\n",
    "    nama = \"Programku\"\n",
    "    versi = \"1.0.2\"\n",
    "    # mengakses variabel lokal\n",
    "    print(\"Nama: %s\" % nama)\n",
    "    print(\"Versi: %s\" % versi)\n",
    "\n",
    "# mengakses variabel global\n",
    "print(\"Nama: %s\" % nama)\n",
    "print(\"Versi: %s\" % versi)\n",
    "\n",
    "# memanggil fungsi help()\n",
    "help()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ae7d0a3-ec9b-4f4d-900e-6af2d6c254aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Variabel global untuk menyimpan data Buku\n",
    "buku = []\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6874b8a6-cfb0-4582-85fd-e87cbd270bc0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fungsi untuk menampilkan semua data\n",
    "def show_data():\n",
    "    if len(buku) <= 0:\n",
    "        print(\"BELUM ADA DATA\")\n",
    "    else:\n",
    "        for indeks in range(len(buku)):\n",
    "            print(\"[%d] %s\" % (indeks, buku[indeks]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79d54b07-c708-406f-9f63-03cef71fdf3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fungsi untuk menambah data\n",
    "def insert_data():\n",
    "    buku_baru = raw_input(\"Judul Buku: \")\n",
    "    buku.append(buku_baru)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "396aa633-e93b-4580-8ae9-5a6fe3e591b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fungsi untuk edit data\n",
    "def edit_data():\n",
    "    show_data()\n",
    "    try:\n",
    "        indeks = int(input(\"Inputkan ID buku: \"))  # konversi ke integer\n",
    "        if indeks >= len(buku):\n",
    "            print(\"ID salah\")\n",
    "        else:\n",
    "            judul_baru = input(\"Judul baru: \")  # gunakan input() di Python 3\n",
    "            buku[indeks] = judul_baru\n",
    "    except ValueError:\n",
    "        print(\"Input harus berupa angka\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1574c30f-7ce0-46ee-8fde-7fa88536f07c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fungsi untuk menghapus data\n",
    "def delete_data():\n",
    "    show_data()\n",
    "    try:\n",
    "        indeks = int(input(\"Inputkan ID buku: \"))  # konversi ke integer\n",
    "        if indeks >= len(buku):\n",
    "            print(\"ID salah\")\n",
    "        else:\n",
    "            buku.remove(buku[indeks])\n",
    "    except ValueError:\n",
    "        print(\"Input harus berupa angka\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d57d936-a1fc-4df2-bfac-fa3ffae26571",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Variabel global untuk menyimpan data Buku\n",
    "buku = []\n",
    "\n",
    "# fungsi untuk menampilkan semua data\n",
    "def show_data():\n",
    "    if len(buku) <= 0:\n",
    "        print(\"BELUM ADA DATA\")\n",
    "    else:\n",
    "        for indeks in range(len(buku)):\n",
    "            print(\"[%d] %s\" % (indeks, buku[indeks]))\n",
    "\n",
    "# fungsi untuk menambah data\n",
    "def insert_data():\n",
    "    buku_baru = input(\"Judul Buku: \")  # ganti raw_input() dengan input()\n",
    "    buku.append(buku_baru)\n",
    "\n",
    "# fungsi untuk edit data\n",
    "def edit_data():\n",
    "    show_data()\n",
    "    try:\n",
    "        indeks = int(input(\"Inputkan ID buku: \"))  # konversi ke integer\n",
    "        if indeks >= len(buku):\n",
    "            print(\"ID salah\")\n",
    "        else:\n",
    "            judul_baru = input(\"Judul baru: \")  # ganti raw_input() dengan input()\n",
    "            buku[indeks] = judul_baru\n",
    "    except ValueError:\n",
    "        print(\"Input harus berupa angka!\")\n",
    "\n",
    "# fungsi untuk menghapus data\n",
    "def delete_data():\n",
    "    show_data()\n",
    "    try:\n",
    "        indeks = int(input(\"Inputkan ID buku: \"))  # konversi ke integer\n",
    "        if indeks >= len(buku):\n",
    "            print(\"ID salah\")\n",
    "        else:\n",
    "            buku.remove(buku[indeks])\n",
    "    except ValueError:\n",
    "        print(\"Input harus berupa angka!\")\n",
    "\n",
    "# fungsi untuk menampilkan menu\n",
    "def show_menu():\n",
    "    print(\"\\n\")\n",
    "    print(\"----------- MENU ----------\")\n",
    "    print(\"[1] Show Data\")\n",
    "    print(\"[2] Insert Data\")\n",
    "    print(\"[3] Edit Data\")\n",
    "    print(\"[4] Delete Data\")\n",
    "    print(\"[5] Exit\")\n",
    "    \n",
    "    try:\n",
    "        menu = int(input(\"PILIH MENU> \"))  # konversi ke integer\n",
    "        print(\"\\n\")\n",
    "\n",
    "        if menu == 1:\n",
    "            show_data()\n",
    "        elif menu == 2:\n",
    "            insert_data()\n",
    "        elif menu == 3:\n",
    "            edit_data()\n",
    "        elif menu == 4:\n",
    "            delete_data()\n",
    "        elif menu == 5:\n",
    "            exit()\n",
    "        else:\n",
    "            print(\"Salah pilih!\")\n",
    "    except ValueError:\n",
    "        print(\"Input harus berupa angka!\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    while(True):\n",
    "        show_menu()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
