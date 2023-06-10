function copyPassword() {
  const passwordTextbox = document.querySelector('.password-textbox');
  passwordTextbox.select();
  document.execCommand('copy');

  // Trigger input event
  passwordTextbox.dispatchEvent(new Event('input'));
}

window.onload = function() {
  const lengthSlider = document.querySelector('#length');
  const lengthDisplay = document.querySelector('#length-display');

  lengthDisplay.innerHTML = lengthSlider.value;

  lengthSlider.addEventListener('input', function() {
    lengthDisplay.innerHTML = lengthSlider.value;
  });
}


