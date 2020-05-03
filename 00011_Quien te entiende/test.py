describe 'Interfaz de':
  it 'Mercedes':
    expect(interfaz_mercedes).to match_array ['cantar!']


  it 'Pepita':
    expect(interfaz_pepita).to match_array ['energia', 'cantar!', 'comer_lombriz!', 'volar_en_circulos!']


  it 'Norita':
    expect(interfaz_norita).to match_array ['cantar!', 'comer_lombriz!', 'volar_en_circulos!']

