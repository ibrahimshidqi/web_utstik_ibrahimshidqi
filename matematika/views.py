from django.shortcuts import render

# Create your views here.
def layananmtk(request):
    judul = "Menghasilkan Program Studi Pendidikan Matematika sebagai lembaga bermutu dalam bidang Pendidikan Matematika dan berdaya saing di kawasan ASEAN", "Mewujudkan dosen dan pegawai di Program Studi Pendidikan Matematika yang bermutu dan kompeten", "Menghasilkan lulusan Program Studi Pendidikan Matematika yang unggul, berkarakter, dan berdaya saing di Kawasan ASEAN", "Program Studi Pendidikan Matematika menghasilkan produktivitas penelitian dan pengabdian masyarakat yang tinggi", "Program Studi Pendidikan Matematika menghasilkan publikasi dosen yang bereputasi internasional", "Program Studi Pendidikan Matematika menghasilkan hilirisasi riset yang dapat dimanfaatkan para pemangku kepentingan", "Program Studi Pendidikan Matematika membantu FKIP dalam menghasilkan daya dukung kelembagaan yang bermutu dan berdaya saing", "Program Studi Pendidikan Matematika membantu FKIP dalam menghasilkan sistem monitoring dan evaluasi tata kelola yang berkelanjutan"

    konteks = {
        'judul': judul
    }
    return render(request, 'matematika.html', konteks)
