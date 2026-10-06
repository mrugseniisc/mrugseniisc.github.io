// Obfuscation deters ordinary address harvesting; this is not access control.
const reveal = document.querySelector("#reveal-email");
const details = document.querySelector("#contact-details");
const encoded = [62, 33, 38, 52, 32, 54, 61, 61, 52, 19, 52, 62, 50, 58, 63, 125, 48, 60, 62];

reveal.addEventListener("click", (event) => {
  if (!event.isTrusted) return;
  const address = String.fromCharCode(...encoded.map((value) => value ^ 83));
  const link = document.createElement("a");
  link.className = "contact-address";
  link.href = "mailto:" + address;
  link.textContent = address;
  const hint = document.createElement("p");
  hint.textContent = "Select the address to open your email app, or copy it into a message.";
  details.replaceChildren(link, hint);
  details.hidden = false;
  reveal.setAttribute("aria-expanded", "true");
  reveal.hidden = true;
  link.focus();
});
