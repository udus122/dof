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

//（イベントのトリガーはページの更新？どれかのボタンが押されること？）
//　→　9秒後に「どちらでもない」がclickされる。
//いずかれの選択肢がクリックされたら次の問題へ行く。(更新される)
//progressbarも再開される。

var answerIsYes = document.getElementById("answerIsYes");
var answerIsNeither = document.getElementById("answerIsNeither");
var answerIsNo = document.getElementById("answerIsNo");

//ページをリロードするための関数
function doReload() {
  window.location.reload();
}

//ページが表示されたら9秒後にリロードする処理
window.addEventListener("load", function() {
  setTimeout(doReload, 9000);
});

answerIsNeither.addEventListener("click", function() {});
