/**
 * ỨNG DỤNG HỌC TẬP: BẢNG TUẦN HOÀN CÁC NGUYÊN TỐ HÓA HỌC (KHTN 7)
 * Live Web App URL: https://script.google.com/macros/s/AKfycbynefdy9sF4YOx3ZhFkI7-kkMdm8KpXG8Cd8OGqYPWh6XGVr_BMqa-19UwgJ4kQ70TL/exec
 */

function doGet(e) {
  var possibleNames = ['Index', 'index', 'Index.html', 'index.html', 'Page', 'page', 'Trangchu', 'Home', 'home'];
  var htmlOutput = null;

  for (var i = 0; i < possibleNames.length; i++) {
    try {
      htmlOutput = HtmlService.createHtmlOutputFromFile(possibleNames[i]);
      if (htmlOutput) break;
    } catch (err) {}
  }

  if (!htmlOutput) {
    return HtmlService.createHtmlOutput(
      '<div style="font-family: Arial, sans-serif; padding: 30px; text-align: center; background: #0f172a; color: #fff; min-height: 100vh;">' +
        '<h2 style="color: #38bdf8;">⚠️ Hướng Dẫn Kích Hoạt Ứng Dụng</h2>' +
        '<p style="color: #cbd5e1;">Vui lòng tạo tệp <b>Index</b> (loại HTML) và dán nội dung từ tệp Index.html vào.</p>' +
      '</div>'
    )
    .setTitle('App Học Tập: Bảng Tuần Hoàn - KHTN 7')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0');
  }

  return htmlOutput
    .setTitle('App Học Tập: Bảng Tuần Hoàn - KHTN 7')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0');
}
