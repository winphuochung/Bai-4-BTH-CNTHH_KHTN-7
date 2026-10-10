const QUIZ_DATA = [
  // ================= 1. TRẮC NGHIỆM NHIỀU LỰA CHỌN (1-10) =================
  {
    id: 1,
    type: 'choice',
    category: 'Trắc nghiệm nhiều lựa chọn',
    question: 'Các nguyên tố trong bảng tuần hoàn được sắp xếp theo chiều tăng dần của yếu tố nào sau đây?',
    options: [
      'Khối lượng nguyên tử',
      'Điện tích hạt nhân',
      'Số neutron',
      'Bán kính nguyên tử'
    ],
    answer: 1,
    explanation: 'Theo nguyên tắc sắp xếp hiện đại, các nguyên tố hóa học trong bảng tuần hoàn được sắp xếp theo chiều tăng dần của điện tích hạt nhân (Z).'
  },
  {
    id: 2,
    type: 'choice',
    category: 'Trắc nghiệm nhiều lựa chọn',
    question: 'Các nguyên tố có cùng số lớp electron trong nguyên tử được xếp vào cùng một...',
    options: [
      'Ô nguyên tố',
      'Nhóm',
      'Chu kỳ',
      'Phân nhóm phụ'
    ],
    answer: 2,
    explanation: 'Chu kỳ là dãy các nguyên tố mà nguyên tử của chúng có cùng số lớp electron, được sắp xếp theo chiều điện tích hạt nhân tăng dần.'
  },
  {
    id: 3,
    type: 'choice',
    category: 'Trắc nghiệm nhiều lựa chọn',
    question: 'Các nguyên tố trong cùng một nhóm A có tính chất hóa học tương tự nhau vì nguyên tử của chúng có:',
    options: [
      'Cùng số lớp electron',
      'Cùng số electron ở lớp ngoài cùng',
      'Cùng số proton trong hạt nhân',
      'Cùng khối lượng nguyên tử'
    ],
    answer: 1,
    explanation: 'Các nguyên tố trong cùng một nhóm A có số electron ở lớp ngoài cùng bằng nhau (trừ He ở nhóm VIIIA có 2e), do đó có tính chất hóa học tương tự nhau.'
  },
  {
    id: 4,
    type: 'choice',
    category: 'Trắc nghiệm nhiều lựa chọn',
    question: 'Bảng tuần hoàn các nguyên tố hóa học hiện nay có bao nhiêu chu kỳ và bao nhiêu chu kỳ nhỏ?',
    options: [
      '7 chu kỳ (gồm 3 chu kỳ nhỏ và 4 chu kỳ lớn)',
      '8 chu kỳ (gồm 4 chu kỳ nhỏ và 4 chu kỳ lớn)',
      '7 chu kỳ (gồm 4 chu kỳ nhỏ và 3 chu kỳ lớn)',
      '6 chu kỳ (gồm 3 chu kỳ nhỏ và 3 chu kỳ lớn)'
    ],
    answer: 0,
    explanation: 'Bảng tuần hoàn gồm 7 chu kỳ: chu kỳ 1, 2, 3 gọi là chu kỳ nhỏ; chu kỳ 4, 5, 6, 7 gọi là chu kỳ lớn.'
  },
  {
    id: 5,
    type: 'choice',
    category: 'Trắc nghiệm nhiều lựa chọn',
    question: 'Chu kỳ 1 trong bảng tuần hoàn gồm có bao nhiêu nguyên tố hóa học?',
    options: [
      '2 nguyên tố (H và He)',
      '8 nguyên tố',
      '18 nguyên tố',
      '32 nguyên tố'
    ],
    answer: 0,
    explanation: 'Chu kỳ 1 là chu kỳ đặc biệt ngắn nhất, chỉ gồm 2 nguyên tố là Hydrogen (H, Z=1) và Helium (He, Z=2).'
  },
  {
    id: 6,
    type: 'choice',
    category: 'Trắc nghiệm nhiều lựa chọn',
    question: 'Mỗi ô nguyên tố trong bảng tuần hoàn KHÔNG cho biết thông tin trực tiếp nào sau đây?',
    options: [
      'Số hiệu nguyên tử',
      'Ký hiệu hóa học và tên nguyên tố',
      'Khối lượng nguyên tử',
      'Số hạt neutron trong hạt nhân'
    ],
    answer: 3,
    explanation: 'Ô nguyên tố cho biết: Số hiệu nguyên tử (số p, số e, số thứ tự ô), Ký hiệu hóa học, Tên nguyên tố, Khối lượng nguyên tử. Muốn biết số neutron phải tính hiệu số khối và số proton.'
  },
  {
    id: 7,
    type: 'choice',
    category: 'Trắc nghiệm nhiều lựa chọn',
    question: 'Số thứ tự chu kỳ bằng đại lượng nào trong cấu tạo nguyên tử?',
    options: [
      'Số electron lớp ngoài cùng',
      'Số lớp electron của nguyên tử',
      'Số proton trong hạt nhân',
      'Điện tích hạt nhân'
    ],
    answer: 1,
    explanation: 'Số thứ tự của chu kỳ bằng số lớp electron trong nguyên tử của các nguyên tố thuộc chu kỳ đó.'
  },
  {
    id: 8,
    type: 'choice',
    category: 'Trắc nghiệm nhiều lựa chọn',
    question: 'Số thứ tự của nhóm A bằng với đặc điểm nào trong nguyên tử?',
    options: [
      'Số lớp electron',
      'Tổng số hạt electron',
      'Số electron ở lớp ngoài cùng',
      'Số neutron'
    ],
    answer: 2,
    explanation: 'Đối với các nguyên tố nhóm A, số thứ tự của nhóm (bằng số La Mã từ I đến VIII) chính bằng số electron ở lớp ngoài cùng của nguyên tử.'
  },
  {
    id: 9,
    type: 'choice',
    category: 'Trắc nghiệm nhiều lựa chọn',
    question: 'Nhóm VIIIA trong bảng tuần hoàn bao gồm các nguyên tố thuộc loại nào?',
    options: [
      'Kim loại kiềm',
      'Kim loại kiềm thổ',
      'Halogen (phi kim hoạt động mạnh)',
      'Khí hiếm (khí trơ)'
    ],
    answer: 3,
    explanation: 'Nhóm VIIIA là nhóm các nguyên tố khí hiếm (He, Ne, Ar, Kr, Xe, Rn), có lớp vỏ ngoài cùng bền vững (8 electron, riêng He có 2 electron).'
  },
  {
    id: 10,
    type: 'choice',
    category: 'Trắc nghiệm nhiều lựa chọn',
    question: 'Nguyên tố Hydrogen (H) có 1 electron lớp ngoài cùng, được xếp ở đầu nhóm IA nhưng khác các nguyên tố còn lại trong nhóm vì:',
    options: [
      'Hydrogen là kim loại mềm',
      'Hydrogen là một phi kim, không phải kim loại kiềm',
      'Hydrogen có khối lượng lớn hơn',
      'Hydrogen không có proton'
    ],
    answer: 1,
    explanation: 'Hydrogen (H) có Z=1, 1 electron lớp ngoài cùng. Dù đứng ở nhóm IA nhưng H là phi kim (thể khí ở đktc), các nguyên tố còn lại của nhóm IA đều là kim loại kiềm mạnh.'
  },

  // ================= 2. TRẮC NGHIỆM ĐIỀN KHUYẾT (11-20) =================
  {
    id: 11,
    type: 'fill',
    category: 'Trắc nghiệm điền khuyết',
    question: 'Các nguyên tố trong bảng tuần hoàn được sắp xếp theo chiều tăng dần của _____ hạt nhân.',
    blankHint: 'Gợi ý: 2 từ (đ... t...)',
    acceptable: ['điện tích', 'dien tich', 'điện tích hạt nhân'],
    explanation: 'Nguyên tắc 1: Các nguyên tố được xếp theo chiều tăng dần của điện tích hạt nhân (Z).'
  },
  {
    id: 12,
    type: 'fill',
    category: 'Trắc nghiệm điền khuyết',
    question: 'Số thứ tự của chu kỳ bằng số _____ electron trong nguyên tử.',
    blankHint: 'Gợi ý: 1 từ chỉ thành phần cấu trúc vỏ nguyên tử',
    acceptable: ['lớp', 'lop', 'lớp electron'],
    explanation: 'Số thứ tự chu kỳ = số lớp electron của nguyên tử.'
  },
  {
    id: 13,
    type: 'fill',
    category: 'Trắc nghiệm điền khuyết',
    question: 'Số thứ tự của nhóm A bằng số electron ở lớp _____ của nguyên tử.',
    blankHint: 'Gợi ý: vị trí electron liên kết (n... c...)',
    acceptable: ['ngoài cùng', 'ngoai cung', 'ngoài', 'ngoai'],
    explanation: 'Số thứ tự nhóm A = số electron ở lớp ngoài cùng của nguyên tử.'
  },
  {
    id: 14,
    type: 'fill',
    category: 'Trắc nghiệm điền khuyết',
    question: 'Bảng tuần hoàn gồm có tất cả _____ chu kỳ.',
    blankHint: 'Gợi ý: Một chữ số từ 1 đến 9',
    acceptable: ['7', 'bảy', 'bay'],
    explanation: 'Bảng tuần hoàn hiện nay gồm có 7 chu kỳ được đánh số từ 1 đến 7.'
  },
  {
    id: 15,
    type: 'fill',
    category: 'Trắc nghiệm điền khuyết',
    question: 'Các nguyên tố nhóm VIIIA còn được gọi là nhóm các nguyên tố _____.',
    blankHint: 'Gợi ý: 2 từ (khí trơ / k... h...)',
    acceptable: ['khí hiếm', 'khi hiem', 'khí trơ', 'khi tro'],
    explanation: 'Nhóm VIIIA là nhóm các nguyên tố khí hiếm (hay khí trơ).'
  },
  {
    id: 16,
    type: 'fill',
    category: 'Trắc nghiệm điền khuyết',
    question: 'Số hiệu nguyên tử của nguyên tố có giá trị bằng số hạt _____ trong hạt nhân.',
    blankHint: 'Gợi ý: Loại hạt mang điện tích dương',
    acceptable: ['proton', 'p'],
    explanation: 'Số hiệu nguyên tử Z = số đơn vị điện tích hạt nhân = số proton = số electron.'
  },
  {
    id: 17,
    type: 'fill',
    category: 'Trắc nghiệm điền khuyết',
    question: 'Đa số các nguyên tố hóa học trong bảng tuần hoàn thuộc loại nguyên tố _____ (chiếm hơn 80%).',
    blankHint: 'Gợi ý: kim loại / phi kim / khí hiếm',
    acceptable: ['kim loại', 'kim loai'],
    explanation: 'Hơn 80% các nguyên tố trong bảng tuần hoàn là các nguyên tố kim loại (nhóm IA trừ H, IIA, IIIA trừ B, các nhóm B, họ Lantan và Actini).'
  },
  {
    id: 18,
    type: 'fill',
    category: 'Trắc nghiệm điền khuyết',
    question: 'Nguyên tố Oxygen (Z = 8) có 2 lớp electron và 6 electron ngoài cùng, do đó Oxygen thuộc chu kỳ 2, nhóm _____.',
    blankHint: 'Gợi ý: Số La Mã kèm chữ A (ví dụ: VIA)',
    acceptable: ['VIA', 'VI A', '6A', 'via'],
    explanation: 'O (Z=8) có cấu hình e: 2, 6 -> 2 lớp electron (chu kỳ 2) và 6 electron lớp ngoài cùng (nhóm VIA).'
  },
  {
    id: 19,
    type: 'fill',
    category: 'Trắc nghiệm điền khuyết',
    question: 'Khí hiếm duy nhất ở nhóm VIIIA chỉ có 2 electron ở lớp ngoài cùng là _____.',
    blankHint: 'Gợi ý: Tên nguyên tố khí nhẹ sau Hydrogen hoặc ký hiệu He',
    acceptable: ['helium', 'heli', 'he'],
    explanation: 'Helium (He, Z=2) chỉ có 1 lớp electron chứa tối đa 2e bão hòa, được xếp vào nhóm VIIIA cùng các khí hiếm có 8e ngoài cùng.'
  },
  {
    id: 20,
    type: 'fill',
    category: 'Trắc nghiệm điền khuyết',
    question: 'Nhà hóa học người Nga được coi là cha đẻ của bảng tuần hoàn các nguyên tố hóa học là _____.',
    blankHint: 'Gợi ý: Dmitri M...',
    acceptable: ['mendeleev', 'mendeleev dmitri', 'dmitri mendeleev', 'men-đê-lê-ép', 'mendeleev.'],
    explanation: 'Dmitri Ivanovich Mendeleev (1834 - 1907) là nhà hóa học người Nga đã phát minh ra Bảng tuần hoàn các nguyên tố hóa học năm 1869.'
  },

  // ================= 3. TRẮC NGHIỆM GHÉP CỘT (21-30) =================
  {
    id: 21,
    type: 'match',
    category: 'Trắc nghiệm ghép cột',
    question: 'Ghép tên nguyên tố với ký hiệu hóa học tương ứng:',
    pairs: [
      { left: 'Sodium (Natri)', right: 'Na' },
      { left: 'Potassium (Kali)', right: 'K' },
      { left: 'Iron (Sắt)', right: 'Fe' },
      { left: 'Copper (Đồng)', right: 'Cu' }
    ],
    explanation: 'Sodium: Na (Z=11); Potassium: K (Z=19); Iron: Fe (Z=26); Copper: Cu (Z=29).'
  },
  {
    id: 22,
    type: 'match',
    category: 'Trắc nghiệm ghép cột',
    question: 'Ghép nhóm nguyên tố với tên gọi phân loại đặc trưng:',
    pairs: [
      { left: 'Nhóm IA (trừ H)', right: 'Kim loại kiềm' },
      { left: 'Nhóm IIA', right: 'Kim loại kiềm thổ' },
      { left: 'Nhóm VIIA', right: 'Halogen' },
      { left: 'Nhóm VIIIA', right: 'Khí hiếm' }
    ],
    explanation: 'IA: Kim loại kiềm; IIA: Kim loại kiềm thổ; VIIA: Halogen; VIIIA: Khí hiếm (khí trơ).'
  },
  {
    id: 23,
    type: 'match',
    category: 'Trắc nghiệm ghép cột',
    question: 'Ghép nguyên tố với số hiệu nguyên tử (Z) chính xác:',
    pairs: [
      { left: 'Hydrogen (H)', right: 'Z = 1' },
      { left: 'Carbon (C)', right: 'Z = 6' },
      { left: 'Oxygen (O)', right: 'Z = 8' },
      { left: 'Neon (Ne)', right: 'Z = 10' }
    ],
    explanation: 'H có Z=1; C có Z=6; O có Z=8; Ne có Z=10.'
  },
  {
    id: 24,
    type: 'match',
    category: 'Trắc nghiệm ghép cột',
    question: 'Ghép nguyên tố với số electron lớp ngoài cùng của nguyên tử:',
    pairs: [
      { left: 'Lithium (nhóm IA)', right: '1 electron' },
      { left: 'Magnesium (nhóm IIA)', right: '2 electron' },
      { left: 'Aluminium (nhóm IIIA)', right: '3 electron' },
      { left: 'Chlorine (nhóm VIIA)', right: '7 electron' }
    ],
    explanation: 'Số electron ngoài cùng của nguyên tố nhóm A bằng đúng số thứ tự của nhóm.'
  },
  {
    id: 25,
    type: 'match',
    category: 'Trắc nghiệm ghép cột',
    question: 'Ghép chu kỳ với số lượng nguyên tố chứa trong chu kỳ đó:',
    pairs: [
      { left: 'Chu kỳ 1', right: '2 nguyên tố' },
      { left: 'Chu kỳ 2', right: '8 nguyên tố' },
      { left: 'Chu kỳ 3', right: '8 nguyên tố' },
      { left: 'Chu kỳ 4', right: '18 nguyên tố' }
    ],
    explanation: 'Chu kỳ 1 có 2 nguyên tố (H, He); Chu kỳ 2 và 3 mỗi chu kỳ có 8 nguyên tố; Chu kỳ 4 có 18 nguyên tố.'
  },
  {
    id: 26,
    type: 'match',
    category: 'Trắc nghiệm ghép cột',
    question: 'Ghép nguyên tố với loại nguyên tố tương ứng (Kim loại, Phi kim, Khí hiếm):',
    pairs: [
      { left: 'Aluminium (Nhôm)', right: 'Kim loại' },
      { left: 'Sulfur (Lưu huỳnh)', right: 'Phi kim' },
      { left: 'Argon', right: 'Khí hiếm' },
      { left: 'Calcium (Canxi)', right: 'Kim loại' }
    ],
    explanation: 'Al và Ca là kim loại; S là phi kim; Ar là khí hiếm.'
  },
  {
    id: 27,
    type: 'match',
    category: 'Trắc nghiệm ghép cột',
    question: 'Ghép thông tin trong ô nguyên tố với ý nghĩa tương ứng:',
    pairs: [
      { left: 'Số hiệu nguyên tử (Z)', right: 'Số proton trong hạt nhân' },
      { left: 'Ký hiệu hóa học', right: 'Ký hiệu viết tắt tên nguyên tố' },
      { left: 'Tên nguyên tố', right: 'Tên gọi theo chuẩn IUPAC' },
      { left: 'Khối lượng nguyên tử', right: 'Khối lượng tính theo đơn vị amu' }
    ],
    explanation: 'Ô nguyên tố cung cấp 4 thông tin cơ bản: Số hiệu nguyên tử, Ký hiệu hóa học, Tên nguyên tố và Khối lượng nguyên tử.'
  },
  {
    id: 28,
    type: 'match',
    category: 'Trắc nghiệm ghép cột',
    question: 'Ghép nguyên tố với số lớp electron trong vỏ nguyên tử:',
    pairs: [
      { left: 'Helium (He - Chu kỳ 1)', right: '1 lớp electron' },
      { left: 'Carbon (C - Chu kỳ 2)', right: '2 lớp electron' },
      { left: 'Silicon (Si - Chu kỳ 3)', right: '3 lớp electron' },
      { left: 'Potassium (K - Chu kỳ 4)', right: '4 lớp electron' }
    ],
    explanation: 'Nguyên tố ở chu kỳ nào thì nguyên tử của nó có đúng bấy nhiêu lớp electron.'
  },
  {
    id: 29,
    type: 'match',
    category: 'Trắc nghiệm ghép cột',
    question: 'Ghép các khí hiếm với ứng dụng thực tế phổ biến:',
    pairs: [
      { left: 'Helium (He)', right: 'Bơm khí cầu, bóng bay an toàn' },
      { left: 'Neon (Ne)', right: 'Đèn quảng cáo phát sáng màu cam đỏ' },
      { left: 'Argon (Ar)', right: 'Bảo vệ mối hàn kim loại, bóng sợi đốt' },
      { left: 'Xenon (Xe)', right: 'Đèn flash chụp ảnh cường độ cao' }
    ],
    explanation: 'Các khí hiếm có tính trơ và màu phát sáng đặc trưng khi phóng điện nên có nhiều ứng dụng hữu ích trong đời sống.'
  },
  {
    id: 30,
    type: 'match',
    category: 'Trắc nghiệm ghép cột',
    question: 'Ghép nguyên tố phi kim với trạng thái tồn tại ở nhiệt độ phòng (25°C):',
    pairs: [
      { left: 'Nitrogen (N)', right: 'Chất khí không màu' },
      { left: 'Bromine (Br)', right: 'Chất lỏng màu nâu đỏ' },
      { left: 'Carbon (than/kim cương)', right: 'Chất rắn' },
      { left: 'Chlorine (Cl)', right: 'Chất khí màu vàng lục' }
    ],
    explanation: 'Nitrogen và Chlorine là thể khí; Bromine là phi kim dạng lỏng duy nhất ở nhiệt độ thường; Carbon ở thể rắn.'
  },

  // ================= 4. TRẮC NGHIỆM ĐÚNG/SAI (31-40) =================
  {
    id: 31,
    type: 'tf',
    category: 'Trắc nghiệm Đúng/Sai',
    question: 'Bảng tuần hoàn các nguyên tố hóa học được sắp xếp theo chiều tăng dần của khối lượng nguyên tử.',
    options: ['Đúng', 'Sai'],
    answer: 1,
    explanation: 'SAI. Bảng tuần hoàn hiện đại được sắp xếp theo chiều tăng dần của ĐIỆN TÍCH HẠT NHÂN (Z), không phải theo khối lượng nguyên tử.'
  },
  {
    id: 32,
    type: 'tf',
    category: 'Trắc nghiệm Đúng/Sai',
    question: 'Số thứ tự của ô nguyên tố bằng đúng số proton và bằng số electron trong nguyên tử của nguyên tố đó.',
    options: ['Đúng', 'Sai'],
    answer: 0,
    explanation: 'ĐÚNG. Số thứ tự ô = Số hiệu nguyên tử (Z) = Số proton trong hạt nhân = Số electron trong lớp vỏ.'
  },
  {
    id: 33,
    type: 'tf',
    category: 'Trắc nghiệm Đúng/Sai',
    question: 'Các nguyên tố trong cùng một chu kỳ có số electron lớp ngoài cùng bằng nhau.',
    options: ['Đúng', 'Sai'],
    answer: 1,
    explanation: 'SAI. Các nguyên tố trong cùng một chu kỳ có CÙNG SỐ LỚP ELECTRON, còn số electron lớp ngoài cùng tăng dần từ 1 đến 8 (từ trái sang phải).'
  },
  {
    id: 34,
    type: 'tf',
    category: 'Trắc nghiệm Đúng/Sai',
    question: 'Tất cả các nguyên tố thuộc nhóm IA trong bảng tuần hoàn đều là kim loại kiềm.',
    options: ['Đúng', 'Sai'],
    answer: 1,
    explanation: 'SAI. Hydrogen (H) nằm ở đầu nhóm IA nhưng là một PHI KIM, chỉ từ Lithium (Li) trở xuống mới là kim loại kiềm.'
  },
  {
    id: 35,
    type: 'tf',
    category: 'Trắc nghiệm Đúng/Sai',
    question: 'Bảng tuần hoàn gồm có 8 nhóm A (từ IA đến VIIIA) và 8 nhóm B (từ IB đến VIIIB).',
    options: ['Đúng', 'Sai'],
    answer: 0,
    explanation: 'ĐÚNG. Bảng tuần hoàn dạng ngắn/truyền thống chia thành 8 nhóm A và 8 nhóm B (nhóm B chiếm 10 cột do nhóm VIIIB có 3 cột).'
  },
  {
    id: 36,
    type: 'tf',
    category: 'Trắc nghiệm Đúng/Sai',
    question: 'Chu kỳ 2 và chu kỳ 3 mỗi chu kỳ đều có chứa đúng 8 nguyên tố hóa học.',
    options: ['Đúng', 'Sai'],
    answer: 0,
    explanation: 'ĐÚNG. Chu kỳ 2 (từ Li đến Ne) có 8 nguyên tố; Chu kỳ 3 (từ Na đến Ar) cũng có 8 nguyên tố. Cả hai đều là chu kỳ nhỏ.'
  },
  {
    id: 37,
    type: 'tf',
    category: 'Trắc nghiệm Đúng/Sai',
    question: 'Nguyên tố khí hiếm Helium (He) nằm ở nhóm VIIIA có 8 electron ở lớp ngoài cùng.',
    options: ['Đúng', 'Sai'],
    answer: 1,
    explanation: 'SAI. Helium (Z=2) chỉ có 2 electron và lớp vỏ thứ nhất chứa tối đa 2 electron đã bão hòa, do đó nó chỉ có 2 electron ngoài cùng chứ không phải 8.'
  },
  {
    id: 38,
    type: 'tf',
    category: 'Trắc nghiệm Đúng/Sai',
    question: 'Trong bảng tuần hoàn, các nguyên tố kim loại tập trung chủ yếu ở phía trên bên phải của bảng.',
    options: ['Đúng', 'Sai'],
    answer: 1,
    explanation: 'SAI. Các nguyên tố PHI KIM mới tập trung ở phía trên bên phải; còn KIM LOẠI tập trung ở hầu hết phía bên trái, ở giữa (nhóm B) và phía dưới bảng tuần hoàn.'
  },
  {
    id: 39,
    type: 'tf',
    category: 'Trắc nghiệm Đúng/Sai',
    question: 'Đi từ đầu đến cuối một chu kỳ (từ trái sang phải), điện tích hạt nhân của các nguyên tử tăng dần.',
    options: ['Đúng', 'Sai'],
    answer: 0,
    explanation: 'ĐÚNG. Trong một chu kỳ, theo chiều từ trái qua phải, điện tích hạt nhân Z tăng lần lượt từng đơn vị (+1 mỗi ô).'
  },
  {
    id: 40,
    type: 'tf',
    category: 'Trắc nghiệm Đúng/Sai',
    question: 'Các nguyên tố trong cùng nhóm A có tính chất hóa học tương tự nhau vì có số electron lớp ngoài cùng bằng nhau.',
    options: ['Đúng', 'Sai'],
    answer: 0,
    explanation: 'ĐÚNG. Số electron lớp ngoài cùng quyết định tính chất hóa học. Các nguyên tố nhóm A có cùng số e ngoài cùng nên thể hiện tính chất hóa học tương tự nhau.'
  },

  // ================= 5. TỰ LUẬN (CÂU HỎI MỞ) (41-50) =================
  {
    id: 41,
    type: 'essay',
    category: 'Tự luận ngắn',
    question: 'Hãy nêu 3 nguyên tắc cơ bản dùng để sắp xếp các nguyên tố hóa học trong bảng tuần hoàn.',
    keywords: ['điện tích hạt nhân', 'tăng dần', 'lớp electron', 'chu kỳ', 'electron lớp ngoài cùng', 'ngoài cùng', 'nhóm'],
    modelAnswer: 'Ba nguyên tắc sắp xếp:\n1. Các nguyên tố được xếp theo chiều tăng dần của điện tích hạt nhân.\n2. Các nguyên tố có cùng số lớp electron trong nguyên tử được xếp vào cùng một hàng (chu kỳ).\n3. Các nguyên tố có cùng số electron lớp ngoài cùng được xếp vào cùng một cột (nhóm).',
    explanation: 'Đây là 3 nguyên tắc nền tảng xây dựng nên cấu trúc hàng (chu kỳ), cột (nhóm) và thứ tự các ô trong bảng tuần hoàn.'
  },
  {
    id: 42,
    type: 'essay',
    category: 'Tự luận ngắn',
    question: 'Một ô nguyên tố trong bảng tuần hoàn cung cấp cho ta những thông tin cụ thể nào?',
    keywords: ['số hiệu', 'ký hiệu', 'tên', 'khối lượng nguyên tử'],
    modelAnswer: 'Ô nguyên tố cho biết 4 thông tin cơ bản:\n1. Số hiệu nguyên tử (bằng số proton, số electron, số thứ tự ô).\n2. Ký hiệu hóa học của nguyên tố.\n3. Tên nguyên tố.\n4. Khối lượng nguyên tử.',
    explanation: 'Mỗi ô nguyên tố tóm tắt thông tin nhận dạng và khối lượng của một nguyên tố hóa học theo chuẩn quốc tế IUPAC.'
  },
  {
    id: 43,
    type: 'essay',
    category: 'Tự luận ngắn',
    question: 'Nguyên tử nguyên tố X có 11 proton và 3 lớp electron, lớp ngoài cùng có 1 electron. Xác định vị trí (ô, chu kỳ, nhóm) của X trong bảng tuần hoàn.',
    keywords: ['ô 11', 'chu kỳ 3', 'nhóm ia', 'nhóm 1a', 'natri', 'sodium'],
    modelAnswer: 'Vị trí của nguyên tố X:\n- Ô số 11 (vì có 11 proton, Z = 11).\n- Chu kỳ 3 (vì nguyên tử có 3 lớp electron).\n- Nhóm IA (vì có 1 electron ở lớp ngoài cùng).\n(X chính là nguyên tố Sodium - Na).',
    explanation: 'Số thứ tự ô = số p = 11. Số lớp e = 3 => Chu kỳ 3. Số e ngoài cùng = 1 => Nhóm IA.'
  },
  {
    id: 44,
    type: 'essay',
    category: 'Tự luận ngắn',
    question: 'Vì sao các nguyên tố trong cùng một nhóm A lại có tính chất hóa học gần giống nhau?',
    keywords: ['electron ngoài cùng', 'electron lớp ngoài cùng', 'cấu hình', 'hóa trị'],
    modelAnswer: 'Các nguyên tố trong cùng một nhóm A có tính chất hóa học tương tự nhau vì nguyên tử của chúng có cùng số electron ở lớp ngoài cùng. Số electron lớp ngoài cùng chính là yếu tố quyết định khả năng nhường, nhận hoặc góp chung electron khi tham gia liên kết hóa học.',
    explanation: 'Lớp electron ngoài cùng trực tiếp tham gia vào phản ứng hóa học nên số e ngoài cùng bằng nhau dẫn đến phản ứng và tính chất hóa học tương tự.'
  },
  {
    id: 45,
    type: 'essay',
    category: 'Tự luận ngắn',
    question: 'Phân biệt chu kỳ nhỏ và chu kỳ lớn trong bảng tuần hoàn (nêu rõ số lượng chu kỳ và số nguyên tố trong mỗi loại).',
    keywords: ['chu kỳ nhỏ', 'chu kỳ lớn', '1, 2, 3', '4, 5, 6, 7', '2 nguyên tố', '8 nguyên tố', '18 nguyên tố'],
    modelAnswer: '- Chu kỳ nhỏ gồm các chu kỳ 1, 2, 3: Chu kỳ 1 có 2 nguyên tố; chu kỳ 2 và 3 mỗi chu kỳ có 8 nguyên tố.\n- Chu kỳ lớn gồm các chu kỳ 4, 5, 6, 7: Chứa nhiều nguyên tố hơn (chu kỳ 4 và 5 có 18 nguyên tố; chu kỳ 6 có 32 nguyên tố; chu kỳ 7 chưa đầy đủ/32 nguyên tố).',
    explanation: 'Sự phân chia chu kỳ nhỏ và lớn giúp phân biệt các chu kỳ chỉ gồm nguyên tố nhóm A với các chu kỳ có thêm các nguyên tố chuyển tiếp (nhóm B).'
  },
  {
    id: 46,
    type: 'essay',
    category: 'Tự luận ngắn',
    question: 'Tại sao nguyên tố Hydrogen (H) có 1 electron lớp ngoài cùng nhưng lại không được coi là kim loại kiềm?',
    keywords: ['phi kim', 'thể khí', 'tính chất', 'kim loại kiềm'],
    modelAnswer: 'Mặc dù có 1 electron ở lớp ngoài cùng và được đặt ở nhóm IA, Hydrogen là một phi kim (tồn tại ở dạng khí H2 trong điều kiện thường, không có ánh kim, không dẫn điện dẫn nhiệt như kim loại). Trong khi đó, các nguyên tố còn lại của nhóm IA (Li, Na, K...) đều là các kim loại kiềm điển hình.',
    explanation: 'H chỉ có 1 electron duy nhất (vỏ kề cận bão hòa là He với 2e), có xu hướng góp chung hoặc nhận 1e tạo ion H-, mang tính chất của phi kim.'
  },
  {
    id: 47,
    type: 'essay',
    category: 'Tự luận ngắn',
    question: 'Nêu đặc điểm cấu tạo lớp electron ngoài cùng của các nguyên tử khí hiếm và giải thích vì sao chúng rất bền, khó phản ứng hóa học.',
    keywords: ['8 electron', '2 electron', 'heli', 'bền vững', 'bão hòa', 'khó tham gia'],
    modelAnswer: 'Nguyên tử của các nguyên tố khí hiếm có lớp electron ngoài cùng đã bão hòa và bền vững: Helium có 2 electron ngoài cùng (đầy lớp K), các khí hiếm khác (Ne, Ar, Kr, Xe...) đều có 8 electron ngoài cùng. Do cấu trúc electron ngoài cùng đã bền vững tối đa, chúng rất khó nhường hoặc nhận thêm electron, dẫn đến tính trơ về mặt hóa học.',
    explanation: 'Quy tắc bát tử (8e ngoài cùng) hoặc duet (2e của He) tạo nên trạng thái năng lượng thấp và ổn định nhất của nguyên tử.'
  },
  {
    id: 48,
    type: 'essay',
    category: 'Tự luận ngắn',
    question: 'Một nguyên tử có điện tích hạt nhân là +16. Hãy cho biết tên nguyên tố, ký hiệu, số electron và xác định vị trí của nó (chu kỳ, nhóm) trong bảng tuần hoàn.',
    keywords: ['sulfur', 'lưu huỳnh', 's', '16 electron', 'chu kỳ 3', 'nhóm via', 'nhóm 6a'],
    modelAnswer: '- Điện tích hạt nhân +16 => Số hiệu Z = 16 => Tên: Sulfur (Lưu huỳnh), Ký hiệu: S, có 16 electron.\n- Cấu tạo lớp electron: 2, 8, 6 (có 3 lớp electron và 6 electron ngoài cùng).\n- Vị trí: Ô số 16, Chu kỳ 3, Nhóm VIA.',
    explanation: 'Z = 16 => 3 lớp electron (chu kỳ 3) và lớp ngoài cùng có 6e (nhóm VIA).'
  },
  {
    id: 49,
    type: 'essay',
    category: 'Tự luận ngắn',
    question: 'Hãy chỉ ra ranh giới tương đối giữa kim loại và phi kim trong bảng tuần hoàn và kể tên 3 nguyên tố phi kim phổ biến nhất.',
    keywords: ['bên phải', 'đường bậc thang', 'phi kim', 'oxygen', 'carbon', 'nitrogen', 'hydrogen', 'chlorine'],
    modelAnswer: '- Ranh giới: Các nguyên tố kim loại nằm ở phía bên trái và phía dưới; phi kim nằm ở phía trên bên phải của bảng tuần hoàn (phân tách bởi đường bậc thang chéo).\n- 3 nguyên tố phi kim phổ biến: Oxygen (O), Hydrogen (H), Nitrogen (N) (hoặc Carbon, Chlorine...).',
    explanation: 'Đường ziczac (bậc thang) từ Boron đến Polonium chia bảng tuần hoàn thành mảng kim loại bên trái và phi kim bên phải.'
  },
  {
    id: 50,
    type: 'essay',
    category: 'Tự luận ngắn',
    question: 'Ý nghĩa của bảng tuần hoàn các nguyên tố hóa học đối với việc học tập và nghiên cứu hóa học là gì?',
    keywords: ['dự đoán', 'tính chất', 'liên hệ', 'vị trí', 'cấu tạo'],
    modelAnswer: 'Ý nghĩa của bảng tuần hoàn:\n1. Biết vị trí của một nguyên tố có thể suy ra cấu tạo nguyên tử (số proton, số lớp electron, số electron ngoài cùng) và ngược lại.\n2. Biết vị trí có thể dự đoán được tính chất hóa học cơ bản của nguyên tố đó (là kim loại, phi kim hay khí hiếm, hóa trị cao nhất).\n3. So sánh tính chất của một nguyên tố với các nguyên tố lân cận trong cùng chu kỳ hoặc cùng nhóm.',
    explanation: 'Bảng tuần hoàn là quy luật khái quát hóa thiên tài giúp học sinh không phải học vẹt từng chất mà nắm được quy luật biến đổi chung.'
  }
];\n