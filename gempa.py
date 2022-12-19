class Gempa: 
    # variabel member
    lokasi = ''
    skala  = 0 # variabel static
    GEMPA = 'Gempa Cianjur' # variabel constanta

    # membuat atribute (identitas) atau fungsi constructor
    def __init__(self, lokasi, skala ):
        self.lokasi = lokasi
        self.skala = skala

     # membuat method (perilaku)
    def doSkal(self):
        if(self.skala <= 2):
            skal = "Tidak berasa";
        elif(self.skala >= 2 and self.skala <=4):
            skal = "Retak-retak";
        elif(self.skala <= 4 and self.skala <=6):
            skal = "Bangunan rubuh";
        else:
            skal = "Bangunan rubuh dan berpotensi tsunami";
        print('----------------------------------------------')
        print('skala bencana :',self.skala,
            '\nlokasi bencana :',self.lokasi,
            '\ndampak bencana :',skal)
            














