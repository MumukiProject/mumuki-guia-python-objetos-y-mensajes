describe 'Interfaz de' do
  it 'Mercedes' do
    expect(interfaz_mercedes).to match_array ['cantar!']
  end

  it 'Pepita' do
    expect(interfaz_pepita).to match_array ['energia', 'cantar!', 'comer_lombriz!', 'volar_en_circulos!']
  end

  it 'Norita' do
    expect(interfaz_norita).to match_array ['cantar!', 'comer_lombriz!', 'volar_en_circulos!']
  end  
end