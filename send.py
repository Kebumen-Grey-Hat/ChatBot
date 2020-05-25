function myFunction() {
  var Email = "you@domain.com"
  var Sbj = "Subject"
  var msg = "Body"
  var i =0 //Dont change this
  var qty = 50 //Number of messages to send.
  while(i<qty){
  MailApp.sendEmail(Email, Sbj, msg);
    i++
  }
}
