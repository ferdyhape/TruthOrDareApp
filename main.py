import streamlit as st
import random

# set page config
st.set_page_config(
    page_title="TOD Game App | FERDYHAPE", 
    page_icon=":gear:",
    layout="centered", 
    initial_sidebar_state="auto", menu_items=None
    )

# sidebar for author introduction
st.sidebar.markdown("""

<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"
        integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
    <div class="profile_picture">
        <img src="https://github.com/ferdyhape.png" alt="Profile_Picture" srcset="">
    </div>
    <p class ="html" style='text-align: center;'>Connect with me!</p>
    <div class="group-icon">
        <a href="https://github.com/ferdyhape" target="_blank"><i class="fa-brands fa-github"></i></a>
        <a href="https://instagram.com/ferdyhape" target="_blank"><i class="fa-brands fa-instagram"></i></a>
        <a href="https://www.linkedin.com/in/ferdy-hahan-pradana/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
    </div> 
    <footer>
        <p class="copyright">©2023<br> Copyright By <a href="https://github.com/ferdyhape">FERDYHAPE</a></p>
    </footer>
    <style>
    .profile_picture {
        text-align:center;
    }
    .profile_picture img{
      border-radius: 50%;
      width: 65%;
    }
    .group-icon {
        margin: 10px 20px;
        padding: 0;
        border-radius: 25px;
        background-color: #F6F6F6;
        text-align: center;
        font-size: 25px;
    } 
    .group-icon:hover {
        background-color: #F9F9F9;
        cursor: pointer;
    }
    .fa-github {
        color: #333;
    }
    .fa-instagram {
        color: #833AB4;
    }
    .fa-linkedin {
        color: #0e76a8;
    }
    .author {
        margin: 0px 10px;;
        font-size: 20px;
        font-weight: bold;
    }
    .html {
        margin: 10px 10px;
        padding: 0;
    }
    footer {
        position: static;
        height: 280px;
        width: 100%;
    }
    .copyright{
        position: absolute;
        width: 100%;
        color: #fff;
        line-height: 20px;
        font-size: 1em;
        text-align: center;
        bottom:0;
    }
    .copyright a {
        margin: 0;
        text-decoration: none;
    }
    footer p {
        margin: 0;
    }
    a {
        font-weight: bolder;
        margin: 0 10px;
    }
    </style>
</body>

""", unsafe_allow_html=True)

# set the title of page
def title_template(title):
    st.title(f"""
    {title}
    """)

truth_questions = [
    'Apa kamu pernah selingkuh?',
    'Apa kamu selingkuh sekarang?',
    'Kapan terakhir kali kamu bohong sama aku?',
    'Maukah kau meninggalkanku demi perempuan yang lebih baik daripada aku? Apa alasannya?',
    'Apakah kamu naksir seseorang di tempat kerja?',
    'Jika aku meninggal, berapa lama kamu akan menunggu untuk mendapatkan pasangan baru?',
    'Pernah bohongi aku nggak? Kalau pernah, bohong tentang apa?',
    'Apakah kamu menyimpan rahasia dariku? Apa itu?',
    'Apakah kamu menerimaku apa adanya?',
    'Jika ternyata aku memiliki kekurangan yang jauh dari ekspektasimu, bagaimana cara kamu menyikapinya?',
    'Jawab jujur, apakah kamu pernah merasa bosan menjalani hubungan denganku?',
    'Apa yang akan kamu lakukan jika salah satu dari kita mengalami fase jenuh di dalam hubungan ini?',
    'Bagaimana jika kelak kita diharuskan untuk menjalin hubungan jarak jauh?',
    'Bagaimana responsmu, ketika aku didekati oleh laki-laki atau perempuan lain?',
    'Kalau mantanku mendekatiku lagi, apa yang akan kamu lakukan?',
    'Jika ternyata aku bukan jodohmu, bagaimana tanggapanmu?',
    'Sampai kapan kamu akan mencintaiku?',
    'Jika kelak aku tertimpa musibah dan mengalami kerugian yang berarti, apa yang akan kamu lakukan?',
    'Punya celebrity crush? Siapa?',
    'Biasanya siapa yang kamu stalking di Instagram?',
    'Apa love language kamu?',
    'Hal apa yang dapat membuatmu merasa anxiety?',
    'Situasi apa yang membuat kamu bahagia?',
    'Sesuatu atau tindakan buruk apa yang pernah kamu lakukan?',
    'Apa kebiasaan burukmu dari lahir?',
    'Pernah bohong ke orangtua? Kalau pernah, tentang apa?',
    'Hubungan siapa yang kamu kagumi dan mengapa?',
    'Bagaimana cara kamu menenangkan diri?',
    'Apa hal tergila yang pernah kamu lakukan?',
    'Apa saja fakta memalukan tentang dirimu?',
    'Kapan terakhir menangis? Kenapa?',
    'Apa ketakutan terbesarmu?',
    'Apa aib yang kamu sembunyikan dari aku?',
    'Bagaimana cara kamu menyelesaikan masalah?',
    'Apa penyesalan terbesarmu?',
    'Apa pendapat kamu mengenai hubungan yang sehat?',
    'Apa saja hal yang kamu anggap penting?',
    'Sikap seperti apa yang membuatmu merasa diperlakukan dengan spesial?',
    'Apa saja hal-hal kecil yang bisa membuatmu kesal?',
    'Apa kegiatan paling menantang yang ingin kamu lakukan, namun belum sempat terwujud?',
    'Pernah cemburu berat? Apa yang bikin kamu cemburu?',
    'Apa nama aku yang kamu simpan di kontak ponselmu?',
    'Apa kamu puas dengan hubungan kita saat ini?',
    'Apa hal paling berat dalam menjalani hubungan denganku?',
    'Apakah kamu mau jadi pasanganku selamanya? Apa rencana masa depanmu denganku?',
    'Bagaimana perasaanmu jika sedang bersama denganku?',
    'Apa pendapat kamu tentang pernikahan?',
    'Apa yang ingin kamu wujudkan dari hubungan kita?',
    'Bagaimana kesan pertamamu padaku?',
    'Menurut kamu aku ini orangnya seperti apa?',
    'Menurut kamu apa kekurangan aku?',
    'Apa bukti kalau kamu memang sayang sama aku?',
    'Kamu nggak pernah capek kan jalanin hubungan ini? Apa alasannya?',
    'Pernah kesal dengan aku, tapi kamu memilih bungkam nggak? Kalau ada tentang apa?',
    'Apakah ada aspek hubungan kita yang perlu diperbaiki?',
    'Kebiasaan atau sikapku yang paling menyebalkan menurutmu?',
    'Apa hal yang paling kamu sukai tentang aku?',
    'Apa yang membuat kamu bertahan dengan aku?',
    'Apa pendapat kamu tentang poliamori?',
    'Pasangan seperti apa yang kamu idamkan sebagai pendamping hidupmu?',
]

dare_actions = [
    'Capture dan kirim baris chat Whatsapp teratas kamu',
    'Capture dan kirim baris chat direct message Instagram teratas kamu',
    'Posting foto aku di media sosial',
    'Posting di media sosial dan bilang bahwa kamu sudah putus denganku',
    'Telepon seorang teman dan minta mereka berbohong tentang keberadaanmu kepadaku',
    'Bilang kepada sahabat lawan jenismu kalau kamu menyukainya',
    'Telepon seorang teman, lalu tanyakan apakah kamu pernah membohongiku?',
    'Telepon sahabat terdekat, lalu tanyakan apakah kamu pernah berselingkuh?',
    'Telepon sahabat terdekat, lalu tanyakan apakah ada orang lain yang kamu sukai?',
    'Tunjukkan riwayat akun yang kamu stalk di Instagram',
    'Posting foto memalukan diri sendiri di media sosial',
    'Tirukan salah satu orangtua kamu',
    'Kirim foto memalukan kamu ke orangtua dan keluarga',
    'Tirukan artis favorit kamu',
    'Buat adegan lucu dari film',
    'Melambai ke orang asing dan berpura-pura bahwa kamu mengenalnya',
    'Berjalan ke orang asing dan lakukan hal konyol di depan mereka',
    'Lakukan tarian lucu pada orang asing di sekitarmu',
    'Telepon seorang teman dan teriaki mereka tanpa alasan',
    'Ucapkan sayang kepadaku dengan suara yang keras',
    'Nyanyikan lagu romantis',
    'Nyanyikan lagu dengan namaku',
    'Lakukan hal untuk membuktikan rasa cintamu padaku',
    'Sentuh bagian wajah aku yang menurutmu paling menarik',
    'Baca halaman buku dengan gaya romantis',
    'Buat dan bacakan puisi romantis',
    'Berikan 10 pujian untukku',
    'Ucapkan "I love you" sambil menjawab 10 kali',
    'Sebutkan 5 tentang diriku dengan jujur',
]

def main():
    st.title("Truth or Dare App")
    st.write("Click the button below to get a random Truth and Dare question.")
    columns = st.columns(8)

    if columns[0].button("Truth"):
        question = random.choice(truth_questions)
        st.success(f"Truth: {question}")

    if columns[1].button("Dare"):
        action = random.choice(dare_actions)
        st.success(f"Dare: {action}")

if __name__ == "__main__":
    main()
