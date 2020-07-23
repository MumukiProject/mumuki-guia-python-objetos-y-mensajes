describe 'Pepita':
  before(:each) { Pepita.volar_hacia!(Oberá) }

  it 'vuela a Iruya':
    #...content...#

    expect(Pepita.ciudad).to eq Iruya


  it 'termina con 850 de energía cuando empieza con 1000':
    Pepita.energia = 1000

    #...content...#

    expect(Pepita.energia).to eq 850


  it 'termina con 100 cuando empieza con 700':
    Pepita.energia = 700

    #...content...#

    expect(Pepita.energia).to eq 100

