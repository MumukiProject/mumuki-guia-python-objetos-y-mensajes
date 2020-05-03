describe 'Pepita' do
  before(:each) { Pepita.volar_hacia!(Obera) }
  
  it 'vuela a Iruya' do
    #...content...#

    expect(Pepita.ciudad).to eq Iruya
  end
  
  it 'termina con 850 de energía cuando empieza con 1000' do
    Pepita.energia = 1000
    
    #...content...#
    
    expect(Pepita.energia).to eq 850
  end
  
  it 'termina con 100 cuando empieza con 700' do
    Pepita.energia = 700
  
    #...content...#

    expect(Pepita.energia).to eq 100
  end
end