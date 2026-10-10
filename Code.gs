/**
 * ỨNG DỤNG HỌC TẬP: BẢNG TUẦN HOÀN CÁC NGUYÊN TỐ HÓA HỌC (KHTN 7)
 * Hỗ trợ đồng bộ kết quả bài thi học sinh trực tiếp vào Google Sheets.
 */

// CẤU HÌNH (Tùy chọn): Nếu bạn muốn nộp vào một file Google Sheet có sẵn, hãy dán ID hoặc Link file vào đây (để trống nếu muốn script tự động tạo mới):
var GOOGLE_SHEET_URL = ""; 

/**
 * 1. HÀM KÍCH HOẠT & CẤP QUYỀN (DÙNG ĐỂ BẤM "CHẠY" TRÊN THANH CÔNG CỤ APPS SCRIPT)
 * Chọn hàm KHOI_TAO_HE_THONG và bấm nút "Chạy" để cấp quyền và lấy link Google Sheet.
 */
function KHOI_TAO_HE_THONG() {
  var ss = layHoacTaoBangTinh();
  Logger.log("==================================================");
  Logger.log("✅ KÍCH HOẠT HỆ THỐNG THÀNH CÔNG!");
  Logger.log("📊 LINK BẢNG TÍNH GOOGLE SHEET: " + ss.getUrl());
  Logger.log("==================================================");
  return "Kích hoạt thành công: " + ss.getUrl();
}

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

function layHoacTaoBangTinh() {
  var ss = null;

  // 1. Thử lấy từ biến cấu hình GOOGLE_SHEET_URL nếu người dùng điền
  if (GOOGLE_SHEET_URL && GOOGLE_SHEET_URL.trim() !== "") {
    try {
      var trimmed = GOOGLE_SHEET_URL.trim();
      if (trimmed.indexOf("http") === 0) {
        ss = SpreadsheetApp.openByUrl(trimmed);
      } else {
        ss = SpreadsheetApp.openById(trimmed);
      }
    } catch (e) {
      Logger.log("Không mở được bằng GOOGLE_SHEET_URL: " + e);
    }
  }

  // 2. Thử lấy bảng tính mẹ nếu Apps Script được tạo từ Google Sheets
  if (!ss) {
    try {
      ss = SpreadsheetApp.getActiveSpreadsheet();
    } catch (e) {}
  }

  // 3. Thử lấy ID đã lưu trong ScriptProperties
  var scriptProps = PropertiesService.getScriptProperties();
  if (!ss) {
    var savedId = scriptProps.getProperty("SHEET_ID");
    if (savedId) {
      try {
        ss = SpreadsheetApp.openById(savedId);
      } catch (e) {
        Logger.log("Bảng tính cũ không còn tồn tại, sẽ tạo mới...");
      }
    }
  }

  // 4. Nếu chưa có, tự động tạo mới hoàn toàn (CHỈ CẦN QUYỀN SPREADSHEET, KHÔNG CẦN DRIVEAPP)
  if (!ss) {
    ss = SpreadsheetApp.create("Diem_So_KHTN7_Bang_Tuan_Hoan");
    scriptProps.setProperty("SHEET_ID", ss.getId());
  }

  // Khởi tạo tab và tiêu đề cột
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

  return ss;
}

function recordSubmission(data) {
  var ss = layHoacTaoBangTinh();
  var sheet = ss.getSheetByName("DiemSo_KHTN7") || ss.getActiveSheet();

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
    sheetUrl: ss.getUrl(),
    row: lastRow
  };
}

function saveSubmissionDirect(data) {
  return recordSubmission(data);
}
