---
title: "Contact"
type: page
backlinks: false
description: "Contact Dereje Jima for research collaborations, bioinformatics consultations, mentoring, publication questions, and computational biology projects."
summary: "Contact Dereje Jima for research collaborations, bioinformatics consultations, mentoring, publication questions, and computational biology projects."
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

<form class="contact-form" name="contact" method="POST" action="/contact-thank-you/" netlify data-netlify="true" data-netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact">
  <div class="hidden"><label for="contact-bot-field">Leave this field empty</label><input id="contact-bot-field" name="bot-field"></div>
  <div class="contact-form-header">
    <h2>Send a Message</h2>
    <p>Share a little context and I will respond by email.</p>
  </div>
  <div class="contact-form-grid">
    <div class="contact-form-field"><label for="contact-name">Name</label><input id="contact-name" type="text" name="name" autocomplete="name" required></div>
    <div class="contact-form-field"><label for="contact-email">Email</label><input id="contact-email" type="email" name="email" autocomplete="email" required></div>
  </div>
  <div class="contact-form-field"><label for="contact-topic">Topic</label><select id="contact-topic" name="topic" required><option value="">Select a topic</option><option value="Research collaboration">Research collaboration</option><option value="Bioinformatics consultation">Bioinformatics consultation</option><option value="Mentoring or training">Mentoring or training</option><option value="Publication question">Publication question</option><option value="Other">Other</option></select></div>
  <div class="contact-form-field"><label for="contact-message">Message</label><textarea id="contact-message" name="message" rows="6" maxlength="1200" required></textarea><div class="contact-form-meta"><span id="contact-message-count">0 / 1200</span><span>Required</span></div></div>
  <button type="submit">Send Message</button>
  <p class="contact-form-status" aria-live="polite"></p>
</form>
