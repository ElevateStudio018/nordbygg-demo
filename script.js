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
