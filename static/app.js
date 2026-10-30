const input = document.querySelector('#input');
const output = document.querySelector('#output');
const statusText = document.querySelector('#status');
const translateButton = document.querySelector('#translate');
const source = document.querySelector('#source');
const target = document.querySelector('#target');

document.querySelector('#swap').addEventListener('click', () => {
  [source.value, target.value] = [target.value, source.value];
});

translateButton.addEventListener('click', async () => {
  statusText.textContent = '';
  translateButton.disabled = true;
  translateButton.textContent = 'Translating...';
  try {
    const response = await fetch('/translate', {
      method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({text: input.value, source: source.value, target: target.value})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Something went wrong.');
    output.textContent = data.translated_text;
  } catch (error) {
    statusText.textContent = error.message;
  } finally {
    translateButton.disabled = false;
    translateButton.textContent = 'Translate';
  }
});

document.querySelector('#copy').addEventListener('click', async () => {
  await navigator.clipboard.writeText(output.textContent);
  statusText.textContent = 'Translation copied.';
});
