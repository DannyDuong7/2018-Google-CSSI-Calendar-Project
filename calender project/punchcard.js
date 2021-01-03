const clockInButton = document.querySelector("#clockInButton");
const clockOutButton = document.querySelector("#clockOutButton");
const resetHoursButton = document.querySelector("#resetHoursButton");
var clockedIn = false;
var hourClockedIn;


clockInButton.addEventListener("click",() =>
{
  console.log("Clicked ");
  clockInButton.innerHTML = "Clicked";
  var hourClockedIn = new Date();
  var in_h = hourClockedIn.getHours();
  var in_m = hourClockedIn.getHours();
  var in_s = hourClockedIn.getSeconds();
  in_m = checkTime(in_m);
  in_s = checkTime(in_s);

  alert("You clocked in at " + hourClockedIn + ".");
  clockedIn = true;
});

clockOutButton.addEventListener("click",() =>
{
  clockOutButton.innerHTML = "Clicked";
  var hourClockedOut = new date();
  alert("You clocked out at " + hourClockedOut + " .");
  clockedIn = false;

});

resetHoursButton.addEventListener("click",() =>
{
  clockOutButton.innerHTML = "Clicked";
  if (confirm("Would you like to reset your hours?"))
  {
    alert("You reset your hours.");
  }
  else {
    {
      alert("You did not reset your hours.");
    }
  }

});
if (clockedIn == true)
{
  window.onbeforeunload = function() {
        return "Please clock out before exiting the page.";
}
}
