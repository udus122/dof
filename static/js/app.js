var bar = new ProgressBar.Line(progressBar, {
  strokeWidth: 4,
  easing: "easeInOut",
  duration: 9000,
  color: "orange",
  trailColor: "#f6f5f4",
  trailWidth: 1,
  svgStyle: { width: "100%", height: "100%" }
});
bar.animate(1.0);
