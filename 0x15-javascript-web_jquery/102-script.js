$("document").ready(function () {
    const u = "https://www.fourtonfish.com/hellosalut/?";
    $("INPUT#btn_translate").click(function () {
      $.get(u + $.param({ lang: $("INPUT#language_code").val() }), function (data) {
        $("DIV#hello").html(data.hello);
      });
    });
  });
