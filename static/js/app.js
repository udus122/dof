var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: "horizontalBar",
  data: {
    labels: ["凝縮生", "受容性", "弁別性", "拡散性", "保全性"],
    datasets: [
      {
        label: "特性",
        data: [8, 12, 3, 5, 14],
        // A~EをDBからデータを渡したい。
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)"
        ],
        borderColor: [
          "rgba(255,99,132,1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)"
        ],
        borderWidth: 2
      }
    ]
  },
  options: {
    scales: {
      xAxes: [
        {
          ticks: {
            beginAtZero: true,
            max: 20
          }
        }
      ]
    }
  }
});
