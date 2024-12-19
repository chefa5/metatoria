auth = document.getElementById('auth')
reg = document.getElementById('reg')

voiti = document.getElementById('voiti')
registr = document.getElementById('registr')


registr.onclick = changeonregistr;
voiti.onclick = changeonvoiti;

function changeonregistr() {
    reg.style.display = 'flex'
    auth.style.display = 'none'
  }

  function changeonvoiti() {
    reg.style.display = 'none'
    auth.style.display = 'flex'
  }

