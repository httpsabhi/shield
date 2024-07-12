$(document).ready(function () {
  $("#get-started-button").click(function () {
    window.location.href = "/dashboard";
  });
  
  $("#check-drones").click(function () {
    $.ajax({
      url: "/drones",
      method: "GET",
      success: function (data) {
        $("#drone-status").html("<h2>Drone Status</h2>");
        data.forEach(function (drone) {
          $("#drone-status").append(
            `<p>Drone ${drone.id}: Battery ${drone.battery}%, Available: ${drone.available}, Computing Power: ${drone.computing_power}, Location: ${drone.location}</p>`
          );
        });
      },
    });
  });

  $("#detect-disaster").click(function () {
    $.ajax({
      url: "/detect",
      method: "GET",
      success: function (data) {
        $("#detection-result").html(`<h2>${data.message}</h2>`);
        if (data.mother_drone) {
          $("#detection-result").append(
            `<p>Mother Drone ID: ${data.mother_drone.id}, Battery: ${data.mother_drone.battery}%, Computing Power: ${data.mother_drone.computing_power}</p>`
          );
        }
      },
    });
  });
});
