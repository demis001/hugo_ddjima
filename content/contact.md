---
title: "Contact"
type: page
form:
  provider: netlify
  netlify:
    captcha: true
---

For research collaborations, bioinformatics consultations, trainee mentoring, or questions about my publications, please use the form below.

<div class="contact-qr-panel">
  <div>
    <h2>Scan to Connect</h2>
    <p>Use this QR code to open the contact page quickly on a phone or share it during meetings and events.</p>
    <a href="https://www.ddjima.com/contact/">https://www.ddjima.com/contact/</a>
  </div>
  <img src="/images/contact-qr.png" alt="QR code linking to the Dereje Jima contact page">
</div>

<form class="contact-form" name="contact" method="POST" action="/contact-thank-you/" data-netlify="true" data-netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact">
  <p class="hidden">
    <label>Leave this field empty <input name="bot-field"></label>
  </p>

  <div class="contact-form-grid">
    <label>
      <span>Name</span>
      <input type="text" name="name" autocomplete="name" required>
    </label>

    <label>
      <span>Email</span>
      <input type="email" name="email" autocomplete="email" required>
    </label>
  </div>

  <label>
    <span>Topic</span>
    <select name="topic" required>
      <option value="">Select a topic</option>
      <option value="Research collaboration">Research collaboration</option>
      <option value="Bioinformatics consultation">Bioinformatics consultation</option>
      <option value="Mentoring or training">Mentoring or training</option>
      <option value="Publication question">Publication question</option>
      <option value="Other">Other</option>
    </select>
  </label>

  <label>
    <span>Message</span>
    <textarea name="message" rows="6" required></textarea>
  </label>

  <button type="submit">Send Message</button>
</form>
