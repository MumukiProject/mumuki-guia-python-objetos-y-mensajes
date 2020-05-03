describe 'Interfaz compartida entre' do
  it 'Mercedes y Norita' do
    expect(interfaz_compartida_entre_mercedes_y_norita).to match_array ['cantar!']
  end
  
  it 'Pepita y Norita' do
    expect(interfaz_compartida_entre_pepita_y_norita).to match_array ['cantar!',  'comer_lombriz!', 'volar_en_circulos!']
  end
  
  it 'todas' do
    expect(interfaz_compartida_entre_todas).to match_array ['cantar!']
  end
end