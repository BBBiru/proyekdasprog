#------------------------ Enemy ----------------------
zombie = {
    'Hit': [
        '[HIT] Kamu terkena serangan zombie!',
        '[HIT] Zombie itu berhasil mencakar lenganmu!',
        '[HIT] Zombie itu mengigit bahumu!',
        '[HIT] Kepalamu terkena pukulan zombie!',
        '[HIT] Lehermu terkena goresan kuku zombie!',
        '[HIT] Kepalamu adu hantam dengan kepala zombie!',
        '[HIT] Zombie itu tiba-tiba melempar batu!',
        '[HIT] Kamu terkena damage hanya dengan mencium baunya!',
        '[HIT] Zombie itu memukulmu!',
        '[HIT] Zombie itu mencakar wajahmu!',
    ],
    'Miss': [
        '[MISS] Zombie itu menyerang dan tersandung!',
        '[MISS] Zombie itu tidak mengenaimu!',
        '[MISS] Serangan zombie itu mengenai angin!',
        '[MISS] Kamu berhasil menghindari serangan zombie itu!',
        '[MISS] Serangan zombie itu kejauhan!',
        '[MISS] Kamu lebih cepat dari zombie itu!',
        '[MISS] Kamu menahan serangan zombie itu!',
        '[MISS] Kamu berhasil menjaga jarak dari zombie itu!',
        '[MISS] ',
        '[MISS] ',
    ]
} #ini belom jadi. tadinya tiap serangan mau ada deskripsi kayak gini

#------------------------ Help ----------------------
help_command = {
    'cek' : (
        'Perintah \'cek\' digunakan untuk melihat daftar item dalam kategori tertentu.',
        'Kategori cek: ability, status, buah, equipment.',
        'Contoh penggunaan: cek buah'
    ),
    'jalan' : (
        'Perintah \'jalan\' digunakan untuk memulai perjalanan menjauh dari rumah.',
        'Setiap kali kamu menggunakan perintah ini, posisimu akan bertambah 50 meter.'
    ),
    'exit' : (
        'Perintah \'exit\' digunakan untuk keluar dari permainan.',
    ),
    'equipment' : (
        'Armor berfungsi untuk mengurangi kemungkinanmu terkena serangan musuh.',
        'Weapon adalah senjata yang kamu gunakan.'
    ),
    'objective' : (
        'Tujuan utama game ini adalah mengumpulkan buah-buahan.',
        'Kumpulkan masing-masing 5 dan berhasil kembali ke rumah untuk menyelesaikan permainan'
    )
}

#Nanti fungsi help bakal ngereferensiin ini