(function () {
  var labs = document.querySelectorAll('details.lab');

  function load(d) {
    if (d.dataset.loaded || !d.dataset.src) return;
    d.dataset.loaded = '1';
    var code = d.querySelector('pre code');
    fetch(d.dataset.src)
      .then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.text();
      })
      .then(function (text) {
        code.textContent = text;
        if (window.hljs) hljs.highlightElement(code);
      })
      .catch(function () {
        code.textContent = 'Could not load main.py. Use the file links above instead.';
      });
  }

  labs.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open) load(d);
    });
  });

  function openFromHash() {
    var id = decodeURIComponent(location.hash.slice(1));
    if (!id) return;
    var d = document.getElementById(id);
    if (d && d.classList.contains('lab')) {
      d.open = true;
      load(d);
      d.scrollIntoView();
    }
  }
  window.addEventListener('hashchange', openFromHash);
  openFromHash();
})();
