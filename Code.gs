/**
 * ỨNG DỤNG HỌC TẬP: BẢNG TUẦN HOÀN CÁC NGUYÊN TỐ HÓA HỌC (KHTN 7)
 * Hỗ trợ đồng bộ kết quả bài thi học sinh trực tiếp vào Google Sheets.
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

function doPost(e) {
  try {
    var raw = e.postData.contents;
    var data = JSON.parse(raw);
    var res = recordSubmission(data);
    return ContentService.createTextOutput(JSON.stringify(res))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function recordSubmission(data) {
  var ss = null;
  try {
    ss = SpreadsheetApp.getActiveSpreadsheet();
  } catch (e) {}

  if (!ss) {
    var files = DriveApp.getFilesByName("Diem_So_KHTN7_Bang_Tuan_Hoan");
    if (files.hasNext()) {
      ss = SpreadsheetApp.open(files.next());
    } else {
      ss = SpreadsheetApp.create("Diem_So_KHTN7_Bang_Tuan_Hoan");
    }
  }

  var sheetName = "DiemSo_KHTN7";
  var sheet = ss.getSheetByName(sheetName);
  if (!sheet) {
    sheet = ss.insertSheet(sheetName);
  }

  if (sheet.getLastRow() === 0) {
    var headers = [
      "Thời Gian Nộp",
      "Họ Và Tên",
      "Lớp",
      "Điểm Số (/100)",
      "Số Câu Đúng",
      "Số Câu Đã Làm",
      "Tỷ Lệ Chính Xác",
      "Đánh Giá Học Lực"
    ];
    sheet.appendRow(headers);
    var headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setFontWeight("bold")
      .setBackground("#0284c7")
      .setFontColor("#ffffff")
      .setHorizontalAlignment("center");
    sheet.setFrozenRows(1);
  }

  var timeStr = Utilities.formatDate(new Date(), "GMT+7", "dd/MM/yyyy HH:mm:ss");
  var row = [
    timeStr,
    data.name || "Học sinh",
    data.className || "Lớp 7",
    data.score || 0,
    data.correctCount || 0,
    data.completedCount || 0,
    data.accuracy || "0%",
    data.evaluation || ""
  ];
  sheet.appendRow(row);

  var lastRow = sheet.getLastRow();
  sheet.getRange(lastRow, 1).setHorizontalAlignment("center");
  sheet.getRange(lastRow, 3).setHorizontalAlignment("center");
  sheet.getRange(lastRow, 4).setHorizontalAlignment("center").setFontWeight("bold");
  sheet.getRange(lastRow, 5).setHorizontalAlignment("center");
  sheet.getRange(lastRow, 6).setHorizontalAlignment("center");
  sheet.getRange(lastRow, 7).setHorizontalAlignment("center");

  return {
    status: "success",
    message: "Đã đồng bộ thành công vào Google Sheet!",
    row: lastRow
  };
}

function saveSubmissionDirect(data) {
  return recordSubmission(data);
}
