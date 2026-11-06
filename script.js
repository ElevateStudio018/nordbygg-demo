// 1. Header blir solid efter scroll
const header = document.getElementById('header');
addEventListener('scroll', () => header.classList.toggle('solid', scrollY > 60));
// 2. Mobilmeny
document.getElementById('burger').onclick = () => document.getElementById('nav').classList.toggle('open');
// 3. Element tonas in när de syns (IntersectionObserver)
const io = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  e.target.classList.add('visible');
  if (e.target.classList.contains('count')) countUp(e.target);
  io.unobserve(e.target);
}), { threshold: .2 });
document.querySelectorAll('.reveal, .count').forEach(el => io.observe(el));
// 4. Siffror räknas upp
function countUp(el) {
  const target = +el.dataset.target, t0 = performance.now();
  const step = t => { const p = Math.min((t - t0) / 1500, 1); el.textContent = Math.round(target * p); if (p < 1) requestAnimationFrame(step); };
  requestAnimationFrame(step);
}
// 5. Hero: laddar klippen först när sidan är klar, växlar med övertoning
(() => {
  const vids = [...document.querySelectorAll('#heroVideos video')];
  const dots = [...document.querySelectorAll('#heroDots button')];
  if (!vids.length) return;
  const c = navigator.connection;
  if (c && (c.saveData || /2g/.test(c.effectiveType || ''))) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const suffix = innerWidth < 900 ? '-sm.mp4' : '.mp4';
  let i = 0;
  const load = v => { if (!v.src) { v.src = v.dataset.src + suffix; v.load(); } };
  const show = n => {
    const v = vids[n]; load(v); v.currentTime = 0;
    v.play().then(() => {
      vids.forEach((x, k) => x.classList.toggle('on', k === n));
      dots.forEach((d, k) => d.classList.toggle('on', k === n));
      setTimeout(() => vids.forEach((x, k) => { if (k !== n) x.pause(); }), 900);
    }).catch(() => {});
    i = n;
    load(vids[(n + 1) % vids.length]);
  };
  vids.forEach(v => v.addEventListener('ended', () => show((i + 1) % vids.length)));
  dots.forEach((d, k) => d.addEventListener('click', () => show(k)));
  const start = () => setTimeout(() => show(0), innerWidth < 900 ? 4000 : 1500);
  document.readyState === 'complete' ? start() : addEventListener('load', start);
})();
// 6. Formulär: öppnar e-post med ifyllda uppgifter
document.querySelectorAll('form[data-mailto]').forEach(f => f.addEventListener('submit', e => {
  e.preventDefault();
  const d = new FormData(f), body = [...d].map(([k, v]) => k + ': ' + v).join('\n');
  location.href = 'mailto:' + f.dataset.mailto + '?subject=' + encodeURIComponent('Offertförfrågan – ' + (d.get('Tjänst') || 'Avlopp')) + '&body=' + encodeURIComponent(body);
}));
