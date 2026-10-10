# -*- coding: utf-8 -*-
import sys

with open('quiz_data.js', 'r', encoding='utf-8') as f:
    quiz_code = f.read()

# Make sure quiz_code ends cleanly with ]; and newline
quiz_code = quiz_code.strip()
if quiz_code.endswith(r'\n'):
    quiz_code = quiz_code[:-2]

html_head = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>App Học Tập: Bảng Tuần Hoàn Các Nguyên Tố Hóa Học - KHTN 7</title>
  <!-- Google Fonts & Font Awesome CDN -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- Canvas-confetti & html2canvas -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>

  <style>
    :root {
      --bg-gradient: linear-gradient(135deg, #090d16 0%, #111827 35%, #0f172a 70%, #032030 100%);
      --glass-bg: rgba(255, 255, 255, 0.07);
      --glass-bg-hover: rgba(255, 255, 255, 0.12);
      --glass-border: rgba(255, 255, 255, 0.15);
      --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.45);
      --accent-cyan: #06b6d4;
      --accent-cyan-glow: rgba(6, 182, 212, 0.45);
      --accent-purple: #a855f7;
      --accent-purple-glow: rgba(168, 85, 247, 0.45);
      --accent-emerald: #10b981;
      --accent-rose: #f43f5e;
      --accent-amber: #f59e0b;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-xl: 28px;
      --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Be Vietnam Pro', 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      background: var(--bg-gradient);
      background-attachment: fixed;
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      position: relative;
    }

    /* Ambient Background Glow Circles */
    .bg-blobs {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }
    .blob {
      position: absolute;
      border-radius: 50%;
      filter: blur(100px);
      opacity: 0.28;
      animation: floatSlow 20s infinite alternate ease-in-out;
    }
    .blob-1 {
      width: 450px;
      height: 450px;
      background: #06b6d4;
      top: -120px;
      left: -100px;
    }
    .blob-2 {
      width: 520px;
      height: 520px;
      background: #8b5cf6;
      bottom: -150px;
      right: -100px;
      animation-delay: -5s;
    }
    .blob-3 {
      width: 380px;
      height: 380px;
      background: #ec4899;
      top: 50%;
      left: 45%;
      transform: translate(-50%, -50%);
      animation-delay: -10s;
    }
    @keyframes floatSlow {
      0% { transform: translateY(0) scale(1); }
      100% { transform: translateY(45px) scale(1.12); }
    }

    /* Glass Panels */
    .glass-card {
      background: var(--glass-bg);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      border: 1px solid var(--glass-border);
      box-shadow: var(--glass-shadow);
      border-radius: var(--radius-lg);
      transition: var(--transition);
      position: relative;
      z-index: 1;
    }
    .glass-card:hover {
      border-color: rgba(255, 255, 255, 0.28);
    }

    /* Navigation Bar */
    header.app-header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(9, 13, 22, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--glass-border);
      padding: 0.8rem 1.8rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }
    .brand-logo {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--text-main);
      cursor: pointer;
    }
    .logo-badge {
      width: 52px;
      height: 52px;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 20px var(--accent-cyan-glow);
      overflow: hidden;
      flex-shrink: 0;
      transition: var(--transition);
      background: transparent;
    }
    .logo-badge:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 26px var(--accent-cyan-glow);
    }
    .logo-badge img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      border-radius: 14px;
    }
    .brand-title h1 {
      font-size: 1.15rem;
      font-weight: 800;
      background: linear-gradient(90deg, #38bdf8, #c084fc);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      letter-spacing: -0.02em;
    }
    .brand-title p {
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    .nav-tabs {
      display: flex;
      gap: 8px;
      background: rgba(0, 0, 0, 0.35);
      padding: 5px;
      border-radius: 30px;
      border: 1px solid var(--glass-border);
    }
    .nav-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 8px 18px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: var(--transition);
    }
    .nav-btn:hover {
      color: var(--text-main);
    }
    .nav-btn.active {
      background: linear-gradient(135deg, var(--accent-cyan), #3b82f6);
      color: #fff;
      box-shadow: 0 4px 14px var(--accent-cyan-glow);
    }
    .nav-btn.locked {
      opacity: 0.55;
      cursor: not-allowed;
    }

    .user-nav-wrapper {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .user-profile-badge {
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(255, 255, 255, 0.08);
      padding: 6px 14px;
      border-radius: 30px;
      border: 1px solid var(--glass-border);
      font-size: 0.85rem;
      cursor: pointer;
      transition: var(--transition);
    }
    .user-profile-badge:hover {
      background: rgba(255, 255, 255, 0.15);
      border-color: var(--accent-cyan);
    }
    .user-avatar {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: linear-gradient(135deg, #10b981, #06b6d4);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: bold;
      color: #fff;
    }
    .btn-logout {
      display: none;
      align-items: center;
      gap: 6px;
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #fca5a5;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
    }
    .btn-logout:hover {
      background: rgba(239, 68, 68, 0.3);
      color: #fff;
      border-color: #ef4444;
      transform: translateY(-1px);
    }

    /* Main Container */
    main.main-content {
      flex: 1;
      width: 100%;
      max-width: 1280px;
      margin: 0 auto;
      padding: 1.5rem;
      position: relative;
      z-index: 10;
    }

    /* Screen Views */
    .view-section {
      display: none;
      animation: fadeIn 0.35s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }
    .view-section.active {
      display: block;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(14px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Login Screen - Gateway Modal / View */
    .login-wrapper {
      max-width: 520px;
      margin: 2.5rem auto;
      padding: 2.8rem 2.4rem;
      text-align: center;
      position: relative;
    }
    .login-icon {
      width: 108px;
      height: 108px;
      margin: 0 auto 1.5rem;
      border-radius: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 10px 32px var(--accent-cyan-glow);
      overflow: hidden;
      transition: var(--transition);
      background: transparent;
    }
    .login-icon:hover {
      transform: scale(1.05);
      box-shadow: 0 14px 40px rgba(6, 182, 212, 0.6);
    }
    .login-icon img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      border-radius: 28px;
    }
    .login-title {
      font-family: 'Be Vietnam Pro', 'Plus Jakarta Sans', sans-serif;
      font-size: 1.7rem;
      font-weight: 800;
      margin-bottom: 0.5rem;
      background: linear-gradient(90deg, #38bdf8, #c084fc);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      letter-spacing: -0.01em;
    }
    .login-subtitle {
      color: var(--text-muted);
      font-size: 0.92rem;
      margin-bottom: 2rem;
      line-height: 1.5;
    }
    .form-group {
      margin-bottom: 1.3rem;
      text-align: left;
    }
    .form-group label {
      display: block;
      font-size: 0.88rem;
      font-weight: 600;
      margin-bottom: 0.45rem;
      color: #cbd5e1;
    }
    .form-control {
      width: 100%;
      padding: 13px 16px;
      border-radius: var(--radius-md);
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--glass-border);
      color: #fff;
      font-size: 0.95rem;
      outline: none;
      transition: var(--transition);
    }
    .form-control:focus {
      border-color: var(--accent-cyan);
      box-shadow: 0 0 0 3px var(--accent-cyan-glow);
    }

    .btn-gradient {
      width: 100%;
      padding: 14px;
      border: none;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, var(--accent-cyan), var(--accent-purple));
      color: #fff;
      font-weight: 700;
      font-size: 1rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 4px 18px var(--accent-cyan-glow);
      transition: var(--transition);
    }
    .btn-gradient:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 24px rgba(6, 182, 212, 0.6);
    }
    .btn-secondary {
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
      border: 1px solid var(--glass-border);
      padding: 10px 20px;
      border-radius: var(--radius-md);
      cursor: pointer;
      font-weight: 600;
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.18);
    }

    /* Notification Alert Box */
    .login-alert-banner {
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #fca5a5;
      padding: 12px 16px;
      border-radius: var(--radius-md);
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
      display: none;
      align-items: center;
      gap: 10px;
      text-align: left;
    }

    /* Theory Layout */
    .theory-grid {
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 1.5rem;
    }
    .theory-sidebar {
      position: sticky;
      top: 5rem;
      height: fit-content;
      padding: 1.25rem;
    }
    .theory-nav-item {
      display: block;
      padding: 10px 14px;
      margin-bottom: 6px;
      border-radius: var(--radius-sm);
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
      transition: var(--transition);
    }
    .theory-nav-item:hover, .theory-nav-item.active {
      background: rgba(255, 255, 255, 0.12);
      color: var(--accent-cyan);
      transform: translateX(4px);
    }
    .theory-content-box {
      padding: 2.2rem;
    }
    .theory-header-banner {
      background: linear-gradient(135deg, rgba(6, 182, 212, 0.18), rgba(168, 85, 247, 0.18));
      border: 1px solid var(--glass-border);
      padding: 1.6rem;
      border-radius: var(--radius-lg);
      margin-bottom: 2rem;
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }
    .theory-section-block {
      margin-bottom: 2.8rem;
      scroll-margin-top: 6rem;
    }
    .section-title {
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 1.1rem;
      display: flex;
      align-items: center;
      gap: 10px;
      color: #38bdf8;
    }
    .rule-card {
      background: rgba(0, 0, 0, 0.28);
      border-left: 4px solid var(--accent-cyan);
      padding: 1.1rem 1.3rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-bottom: 1rem;
    }
    .rule-card h4 {
      color: #f1f5f9;
      margin-bottom: 0.35rem;
      font-size: 1.05rem;
    }
    .rule-card p {
      color: var(--text-muted);
      font-size: 0.92rem;
      line-height: 1.6;
    }

    /* Periodic Cell Demo */
    .element-card-demo {
      display: inline-block;
      width: 140px;
      padding: 14px;
      background: rgba(14, 165, 233, 0.15);
      border: 2px solid #38bdf8;
      border-radius: var(--radius-md);
      text-align: center;
      box-shadow: 0 4px 20px rgba(56, 189, 248, 0.25);
      margin: 1rem 0;
    }
    .element-card-demo .atomic-num {
      font-size: 0.9rem;
      text-align: left;
      color: #7dd3fc;
      font-weight: 700;
    }
    .element-card-demo .symbol {
      font-size: 2.5rem;
      font-weight: 800;
      font-family: 'Space Grotesk', sans-serif;
      color: #fff;
      line-height: 1.1;
    }
    .element-card-demo .name {
      font-size: 0.95rem;
      font-weight: 600;
      color: #e0f2fe;
    }
    .element-card-demo .mass {
      font-size: 0.8rem;
      color: #94a3b8;
    }

    /* Video & 3D Section */
    .video-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.5rem;
      margin-top: 1rem;
    }
    .video-card {
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
    }
    
    /* Video Interactive Preview Cards */
    .video-preview-box {
      position: relative;
      width: 100%;
      padding-top: 56.25%;
      border-radius: var(--radius-md);
      overflow: hidden;
      cursor: pointer;
      border: 1px solid var(--glass-border);
      transition: var(--transition);
      background: #0f172a;
    }
    .video-preview-box:hover {
      border-color: var(--accent-cyan);
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(6, 182, 212, 0.3);
    }
    .video-thumb-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at center, rgba(6,182,212,0.25) 0%, rgba(15,23,42,0.95) 75%);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      text-align: center;
    }
    .play-btn-circle {
      width: 68px;
      height: 68px;
      border-radius: 50%;
      background: linear-gradient(135deg, #ef4444, #f43f5e);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.8rem;
      box-shadow: 0 0 25px rgba(239, 68, 68, 0.5);
      margin-bottom: 0.8rem;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .video-preview-box:hover .play-btn-circle {
      transform: scale(1.15);
    }
    .thumb-title {
      font-weight: 700;
      font-size: 1.05rem;
      color: #fff;
      margin-bottom: 0.3rem;
    }
    .thumb-sub {
      font-size: 0.82rem;
      color: var(--text-muted);
      max-width: 80%;
    }
    
    .video-frame-container {
      position: relative;
      width: 100%;
      padding-top: 56.25%;
      border-radius: var(--radius-md);
      overflow: hidden;
      background: #000;
      margin-bottom: 1rem;
    }
    .video-frame-container iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: none;
    }

    /* Interactive 3D Atom Simulator (Canvas) */
    .atom-sim-wrapper {
      background: rgba(0,0,0,0.45);
      border-radius: var(--radius-lg);
      padding: 1.6rem;
      text-align: center;
      margin-top: 1.8rem;
      overflow: hidden;
    }
    #atomCanvas {
      max-width: 100%;
      height: auto;
      aspect-ratio: 5 / 4;
      background: transparent;
      border-radius: var(--radius-md);
      display: block;
      margin: 0 auto;
    }
    .sim-controls {
      display: flex;
      justify-content: center;
      gap: 10px;
      margin-top: 1.2rem;
      flex-wrap: wrap;
      min-height: 48px;
    }
    .sim-btn {
      padding: 8px 16px;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--glass-border);
      color: #cbd5e1;
      font-size: 0.85rem;
      font-weight: 600; /* Co dinh font-weight de khong bi nhay giat layout */
      cursor: pointer;
      transition: background 0.2s ease, color 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
      white-space: nowrap;
      user-select: none;
    }
    .sim-btn.active {
      background: var(--accent-cyan) !important;
      color: #041019 !important;
      border-color: #38bdf8 !important;
      font-weight: 600;
      box-shadow: 0 0 16px var(--accent-cyan-glow);
    }
    .sim-btn:hover:not(.active) {
      background: rgba(255, 255, 255, 0.18);
      color: #fff;
      border-color: rgba(255, 255, 255, 0.3);
    }
    #atomSimInfo {
      min-height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 1.5;
    }

    /* Mini Periodic Table Matrix */
    .table-responsive {
      overflow-x: auto;
      margin: 1.5rem 0;
      padding-bottom: 8px;
    }
    .ptable-grid {
      display: grid;
      grid-template-columns: repeat(18, minmax(42px, 1fr));
      gap: 5px;
      min-width: 820px;
    }
    .p-cell {
      aspect-ratio: 1;
      border-radius: 6px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      cursor: pointer;
      transition: transform 0.2s, box-shadow 0.2s;
      border: 1px solid rgba(255,255,255,0.12);
      padding: 2px;
    }
    .p-cell:hover {
      transform: scale(1.18);
      z-index: 5;
      box-shadow: 0 4px 14px rgba(0,0,0,0.6);
    }
    .p-cell .p-num { font-size: 0.6rem; opacity: 0.75; }
    .p-cell .p-sym { font-weight: 700; font-size: 0.88rem; }
    .p-metal { background: rgba(59, 130, 246, 0.35); border-color: #3b82f6; }
    .p-nonmetal { background: rgba(16, 185, 129, 0.35); border-color: #10b981; }
    .p-noble { background: rgba(245, 158, 11, 0.35); border-color: #f59e0b; }
    .p-empty { visibility: hidden; }

    /* QUIZ SECTION */
    .quiz-layout {
      max-width: 900px;
      margin: 0 auto;
    }
    .quiz-meta-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.1rem 1.6rem;
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
      gap: 1.2rem;
    }
    .quiz-progress-wrap {
      flex: 1;
      min-width: 200px;
    }
    .progress-bar-bg {
      height: 9px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      overflow: hidden;
      margin-top: 6px;
    }
    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple));
      width: 0%;
      transition: width 0.4s ease;
    }
    .score-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 700;
      color: #38bdf8;
      background: rgba(6, 182, 212, 0.15);
      padding: 7px 18px;
      border-radius: 20px;
      border: 1px solid var(--accent-cyan);
    }

    /* Category Filter Tabs */
    .quiz-filters {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 10px;
      margin-bottom: 1.5rem;
    }
    .filter-btn {
      white-space: nowrap;
      padding: 8px 16px;
      border-radius: 20px;
      background: rgba(255,255,255,0.06);
      border: 1px solid var(--glass-border);
      color: var(--text-muted);
      font-size: 0.85rem;
      cursor: pointer;
      transition: var(--transition);
    }
    .filter-btn:hover { color: #fff; }
    .filter-btn.active {
      background: var(--accent-purple);
      color: #fff;
      font-weight: 600;
      border-color: var(--accent-purple);
    }

    .question-box {
      padding: 2.2rem;
      margin-bottom: 1.5rem;
    }
    .q-type-badge {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 6px;
      background: rgba(168, 85, 247, 0.2);
      color: #c084fc;
      border: 1px solid rgba(168, 85, 247, 0.4);
      margin-bottom: 0.75rem;
    }
    .q-title {
      font-size: 1.28rem;
      font-weight: 600;
      line-height: 1.6;
      margin-bottom: 1.6rem;
    }

    /* Choice Options */
    .options-grid {
      display: grid;
      gap: 12px;
    }
    .option-btn {
      width: 100%;
      padding: 14px 18px;
      text-align: left;
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--glass-border);
      color: var(--text-main);
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 14px;
      transition: var(--transition);
    }
    .option-btn:hover:not(:disabled) {
      background: rgba(255, 255, 255, 0.12);
      border-color: var(--accent-cyan);
      transform: translateX(4px);
    }
    .option-btn .opt-prefix {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.85rem;
      flex-shrink: 0;
    }
    .option-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #a7f3d0;
    }
    .option-btn.correct .opt-prefix {
      background: #10b981;
      color: #fff;
    }
    .option-btn.wrong {
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: #f43f5e !important;
      color: #fecdd3;
    }
    .option-btn.wrong .opt-prefix {
      background: #f43f5e;
      color: #fff;
    }

    /* Fill in Blank */
    .fill-input-box {
      display: flex;
      gap: 12px;
      margin-bottom: 1rem;
    }
    .fill-input {
      flex: 1;
      padding: 14px 18px;
      border-radius: var(--radius-md);
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--glass-border);
      color: #fff;
      font-size: 1rem;
      outline: none;
    }

    /* Matching Pairs Style */
    .match-columns {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 1.5rem;
    }
    .match-item {
      padding: 13px 16px;
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.05);
      border: 2px solid var(--glass-border);
      cursor: pointer;
      margin-bottom: 10px;
      font-size: 0.92rem;
      transition: var(--transition);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .match-item:hover {
      background: rgba(255, 255, 255, 0.12);
    }
    .match-item.selected {
      border-color: var(--accent-cyan);
      background: rgba(6, 182, 212, 0.2);
    }
    .match-item.matched {
      border-color: var(--accent-emerald);
      background: rgba(16, 185, 129, 0.2);
      pointer-events: none;
      opacity: 0.85;
    }

    /* Essay Question */
    .essay-textarea {
      width: 100%;
      height: 120px;
      padding: 14px;
      border-radius: var(--radius-md);
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--glass-border);
      color: #fff;
      font-size: 0.95rem;
      resize: vertical;
      margin-bottom: 1rem;
      outline: none;
    }

    /* Explanation Accordion */
    .explanation-box {
      margin-top: 1.5rem;
      padding: 1.25rem;
      border-radius: var(--radius-md);
      background: rgba(0, 0, 0, 0.35);
      border-left: 4px solid var(--accent-purple);
      animation: fadeIn 0.3s ease;
      display: none;
    }
    .explanation-box.show {
      display: block;
    }
    .exp-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: #c084fc;
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .exp-text {
      color: #cbd5e1;
      font-size: 0.9rem;
      line-height: 1.6;
    }

    /* Action Nav Buttons (Prev/Next) */
    .quiz-nav-actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 1.5rem;
    }

    /* Result View & Certificate */
    .result-wrapper {
      max-width: 680px;
      margin: 2rem auto;
      padding: 2.8rem;
      text-align: center;
    }
    .result-header-icon {
      width: 90px;
      height: 90px;
      border-radius: 50%;
      background: linear-gradient(135deg, #10b981, #06b6d4);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.5rem;
      color: #fff;
      margin: 0 auto 1.5rem;
      box-shadow: 0 10px 30px rgba(16, 185, 129, 0.4);
    }
    .result-score-circle {
      font-size: 3.5rem;
      font-weight: 800;
      font-family: 'Space Grotesk', sans-serif;
      background: linear-gradient(90deg, #38bdf8, #a855f7);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 0.5rem;
    }
    .result-stats-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 15px;
      margin: 2rem 0;
    }
    .stat-pill {
      background: rgba(255, 255, 255, 0.06);
      padding: 1rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--glass-border);
    }
    .stat-val {
      font-size: 1.4rem;
      font-weight: 700;
      color: #fff;
    }
    .stat-lbl {
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-top: 4px;
    }

    /* Leaderboard */
    .leaderboard-box {
      margin-top: 2rem;
      text-align: left;
    }
    .leader-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 16px;
      border-radius: var(--radius-sm);
      margin-bottom: 8px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--glass-border);
      font-size: 0.92rem;
    }
    .leader-rank {
      font-weight: 800;
      width: 28px;
    }
    .rank-1 { color: #fbbf24; }
    .rank-2 { color: #94a3b8; }
    .rank-3 { color: #b45309; }

    /* Shake Screen Effect */
    @keyframes shakeScreen {
      0%, 100% { transform: translateX(0); }
      20%, 60% { transform: translateX(-8px); }
      40%, 80% { transform: translateX(8px); }
    }
    .shake-anim {
      animation: shakeScreen 0.4s ease-in-out;
    }

    /* Mobile Responsive */
    @media (max-width: 768px) {
      .theory-grid {
        grid-template-columns: 1fr;
      }
      .theory-sidebar {
        display: none;
      }
      .match-columns {
        grid-template-columns: 1fr;
      }
      .brand-title h1 {
        font-size: 1rem;
      }
      .brand-title p {
        display: none;
      }
      .nav-tabs {
        overflow-x: auto;
      }
      .nav-btn {
        padding: 6px 12px;
        font-size: 0.78rem;
      }
    }
  </style>
</head>
<body>

  <!-- Ambient Glowing Blobs -->
  <div class="bg-blobs">
    <div class="blob blob-1"></div>
    <div class="blob blob-2"></div>
    <div class="blob blob-3"></div>
  </div>

  <!-- Header Navigation -->
  <header class="app-header">
    <div class="brand-logo" onclick="handleBrandClick()">
      <div class="logo-badge">
        <img src="logo.png" alt="Logo KHTN 7" onerror="this.parentElement.innerHTML='<i class=\'fa-solid fa-atom\' style=\'font-size:1.6rem; color:#fff;\'></i>'">
      </div>
      <div class="brand-title">
        <h1>KHTN 7: BẢNG TUẦN HOÀN</h1>
        <p>Học tập & tương tác trực quan thông minh</p>
      </div>
    </div>

    <nav class="nav-tabs" id="mainNavTabs">
      <button class="nav-btn" id="tabTheory" onclick="switchView('theory')">
        <i class="fa-solid fa-book-open"></i> <span>Lý Thuyết</span>
      </button>
      <button class="nav-btn" id="tabVideo" onclick="switchView('video')">
        <i class="fa-solid fa-play"></i> <span>Video & 3D</span>
      </button>
      <button class="nav-btn" id="tabQuiz" onclick="switchView('quiz')">
        <i class="fa-solid fa-circle-question"></i> <span>Luyện Tập (50 Câu)</span>
      </button>
      <button class="nav-btn" id="tabLeaderboard" onclick="switchView('leaderboard')">
        <i class="fa-solid fa-trophy"></i> <span>Xếp Hạng</span>
      </button>
    </nav>

    <div class="user-nav-wrapper">
      <div class="user-profile-badge" id="userBadge" onclick="showLoginModal()">
        <div class="user-avatar" id="avatarLetter">?</div>
        <span id="userNameDisplay">Đăng nhập</span>
      </div>
      <button class="btn-secondary" onclick="copyAppShareLink()" title="Sao chép liên kết chia sẻ ứng dụng" style="padding:6px 14px; font-size:0.82rem; border-radius:20px;">
        <i class="fa-solid fa-share-nodes"></i> <span>Chia sẻ link</span>
      </button>
      <button class="btn-logout" id="btnLogout" onclick="handleLogout()" title="Đăng xuất khỏi tài khoản">
        <i class="fa-solid fa-arrow-right-from-bracket"></i> <span>Đăng xuất</span>
      </button>
    </div>
  </header>

  <!-- Main Container -->
  <main class="main-content">

    <!-- 1. VIEW: LOGIN GATEWAY (CỔNG ĐĂNG NHẬP BẮT BUỘC) -->
    <section class="view-section active" id="viewLogin">
      <div class="login-wrapper glass-card">
        <div class="login-icon">
          <img src="logo.png" alt="Logo KHTN 7" onerror="this.parentElement.innerHTML='<i class=\'fa-solid fa-graduation-cap\' style=\'font-size:2.8rem; color:#fff;\'></i>'">
        </div>
        <h2 class="login-title">CỔNG ĐĂNG NHẬP HỌC SINH</h2>
        <p class="login-subtitle">
          Vui lòng nhập <strong>Họ tên</strong> và <strong>Lớp</strong> để mở khóa bài học, làm bài tập và ghi nhận điểm số!
        </p>

        <div class="login-alert-banner" id="loginAlert">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <span>Em cần đăng nhập trước để truy cập vào bài học và luyện tập!</span>
        </div>

        <form id="loginForm" onsubmit="handleLoginSubmit(event); return false;" autocomplete="off">
          <div class="form-group">
            <label for="inputStudentName"><i class="fa-solid fa-user"></i> Họ và Tên học sinh</label>
            <input type="text" id="inputStudentName" class="form-control" placeholder="Ví dụ: Nguyễn Văn An" required autocomplete="name">
          </div>
          <div class="form-group">
            <label for="inputStudentClass"><i class="fa-solid fa-school"></i> Lớp học</label>
            <input type="text" id="inputStudentClass" class="form-control" placeholder="Ví dụ: 7A1" required autocomplete="off">
          </div>
          <button type="button" id="btnLoginSubmit" class="btn-gradient" style="margin-top: 1rem; width: 100%; cursor: pointer;" onclick="handleLoginSubmit(event)">
            <span>Vào Học Ngay</span>
            <i class="fa-solid fa-arrow-right"></i>
          </button>
        </form>
      </div>
    </section>

    <!-- 2. VIEW: THEORY (LÝ THUYẾT TRỌNG TÂM) -->
    <section class="view-section" id="viewTheory">
      <div class="theory-grid">
        <!-- Sidebar Navigation -->
        <aside class="theory-sidebar glass-card">
          <h3 style="font-size: 1rem; margin-bottom: 1rem; color: #38bdf8;">
            <i class="fa-solid fa-list-check"></i> Nội Dung Bài Học
          </h3>
          <a href="#sec1" class="theory-nav-item active"><i class="fa-solid fa-compass"></i> I. Nguyên tắc sắp xếp</a>
          <a href="#sec2" class="theory-nav-item"><i class="fa-solid fa-cubes"></i> II. Cấu tạo bảng tuần hoàn</a>
          <a href="#sec3" class="theory-nav-item"><i class="fa-solid fa-shapes"></i> III. Phân loại nguyên tố</a>
          <a href="#sec4" class="theory-nav-item"><i class="fa-solid fa-table-cells"></i> IV. Bảng tuần hoàn tương tác</a>
        </aside>

        <!-- Main Content Area -->
        <div class="theory-content-box glass-card">
          <!-- Banner -->
          <div class="theory-header-banner">
            <div style="font-size: 3rem; color: #38bdf8;">
              <i class="fa-solid fa-lightbulb"></i>
            </div>
            <div>
              <h2 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 4px;">
                Bài 4: Sơ Lược Về Bảng Tuần Hoàn Các Nguyên Tố Hóa Học
              </h2>
              <p style="color: var(--text-muted); font-size: 0.95rem;">
                Môn Khoa Học Tự Nhiên 7 • Giúp ghi nhớ bản đồ các nguyên tố vũ trụ một cách trực quan, khoa học
              </p>
            </div>
          </div>

          <!-- Section 1 -->
          <div class="theory-section-block" id="sec1">
            <h3 class="section-title"><i class="fa-solid fa-compass"></i> I. Nguyên Tắc Sắp Xếp Các Nguyên Tố Hóa Học</h3>
            <p style="margin-bottom: 1rem; color: #cbd5e1; line-height: 1.6;">
              Năm 1869, nhà hóa học người Nga <strong>Dmitri Mendeleev</strong> đã công bố bảng tuần hoàn đầu tiên. Ngày nay, các nguyên tố được sắp xếp theo <strong>3 nguyên tắc khoa học hiện đại</strong>:
            </p>
            
            <div class="rule-card">
              <h4>1. Theo chiều tăng dần của điện tích hạt nhân</h4>
              <p>Các nguyên tố hóa học được xếp theo thứ tự điện tích hạt nhân (Z = 1, 2, 3...) tăng dần từ trái sang phải, từ trên xuống dưới.</p>
            </div>
            <div class="rule-card">
              <h4>2. Cùng số lớp electron xếp vào cùng 1 hàng (Chu kỳ)</h4>
              <p>Các nguyên tố mà nguyên tử của chúng có cùng số lớp electron được xếp thành một hàng ngang gọi là chu kỳ.</p>
            </div>
            <div class="rule-card">
              <h4>3. Cùng số electron lớp ngoài cùng xếp vào cùng 1 cột (Nhóm)</h4>
              <p>Các nguyên tố có cùng số electron ở lớp ngoài cùng có tính chất hóa học tương tự nhau, được xếp thành một cột dọc gọi là nhóm.</p>
            </div>
          </div>

          <!-- Section 2 -->
          <div class="theory-section-block" id="sec2">
            <h3 class="section-title"><i class="fa-solid fa-cubes"></i> II. Cấu Tạo Của Bảng Tuần Hoàn</h3>
            
            <h4 style="color: #cbd5e1; margin: 1rem 0 0.5rem;"><i class="fa-solid fa-square-check" style="color: #06b6d4;"></i> 1. Ô Nguyên Tố</h4>
            <p style="color: var(--text-muted); line-height: 1.6;">
              Mỗi nguyên tố chiếm một ô trong bảng tuần hoàn, cho ta biết 4 thông tin thiết yếu:
            </p>

            <div style="display: flex; gap: 2rem; align-items: center; flex-wrap: wrap;">
              <div class="element-card-demo">
                <div class="atomic-num">6</div>
                <div class="symbol">C</div>
                <div class="name">Carbon</div>
                <div class="mass">12,011</div>
              </div>
              <ul style="list-style: none; line-height: 2; color: #cbd5e1;">
                <li><strong style="color: #38bdf8;">• Số hiệu nguyên tử (Z):</strong> Bằng số proton, số electron, và số thứ tự ô (Z = 6).</li>
                <li><strong style="color: #38bdf8;">• Ký hiệu hóa học:</strong> C</li>
                <li><strong style="color: #38bdf8;">• Tên nguyên tố:</strong> Carbon</li>
                <li><strong style="color: #38bdf8;">• Khối lượng nguyên tử:</strong> 12,011 amu</li>
              </ul>
            </div>

            <h4 style="color: #cbd5e1; margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-square-check" style="color: #06b6d4;"></i> 2. Chu Kỳ (Dãy hàng ngang)</h4>
            <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.5rem;">
              Bảng tuần hoàn gồm có <strong>7 chu kỳ</strong> được đánh số từ 1 đến 7:
            </p>
            <ul style="padding-left: 1.25rem; color: #cbd5e1; line-height: 1.8;">
              <li><strong>Số thứ tự chu kỳ = Số lớp electron trong nguyên tử.</strong></li>
              <li><strong>Chu kỳ nhỏ (1, 2, 3):</strong> Chu kỳ 1 (2 nguyên tố: H, He); Chu kỳ 2 (8 nguyên tố); Chu kỳ 3 (8 nguyên tố).</li>
              <li><strong>Chu kỳ lớn (4, 5, 6, 7):</strong> Chu kỳ 4 & 5 (mỗi chu kỳ 18 nguyên tố); Chu kỳ 6 (32 nguyên tố); Chu kỳ 7 (chưa hoàn tất).</li>
            </ul>

            <h4 style="color: #cbd5e1; margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-square-check" style="color: #06b6d4;"></i> 3. Nhóm (Cột dọc)</h4>
            <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 0.5rem;">
              Gồm các nguyên tố có cấu hình electron tương tự nhau, được chia thành:
            </p>
            <ul style="padding-left: 1.25rem; color: #cbd5e1; line-height: 1.8;">
              <li><strong>8 nhóm A (từ IA đến VIIIA):</strong> Số thứ tự nhóm A = <strong>Số electron ở lớp ngoài cùng</strong>.</li>
              <li><strong>8 nhóm B (từ IB đến VIIIB):</strong> Các nguyên tố kim loại chuyển tiếp.</li>
            </ul>
          </div>

          <!-- Section 3 -->
          <div class="theory-section-block" id="sec3">
            <h3 class="section-title"><i class="fa-solid fa-shapes"></i> III. Phân Loại Các Nguyên Tố Hóa Học</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
              <div class="glass-card" style="padding: 1.25rem; border-top: 3px solid #3b82f6;">
                <h4 style="color: #60a5fa; margin-bottom: 0.5rem;"><i class="fa-solid fa-shield"></i> Kim Loại</h4>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
                  Chiếm hơn 80% các nguyên tố. Gồm toàn bộ nhóm IA (trừ H), nhóm IIA, nhóm IIIA (trừ B), và tất cả các nhóm B. Có tính dẫn điện, dẫn nhiệt, ánh kim.
                </p>
              </div>
              <div class="glass-card" style="padding: 1.25rem; border-top: 3px solid #10b981;">
                <h4 style="color: #34d399; margin-bottom: 0.5rem;"><i class="fa-solid fa-fire"></i> Phi Kim</h4>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
                  Nằm ở phía trên bên phải của bảng tuần hoàn (nhóm IVA, VA, VIA, VIIA) và Hydrogen ở nhóm IA. Kém dẫn điện, dẫn nhiệt.
                </p>
              </div>
              <div class="glass-card" style="padding: 1.25rem; border-top: 3px solid #f59e0b;">
                <h4 style="color: #fbbf24; margin-bottom: 0.5rem;"><i class="fa-solid fa-gem"></i> Khí Hiếm</h4>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
                  Nhóm VIIIA (He, Ne, Ar, Kr, Xe, Rn). Có lớp electron ngoài cùng bão hòa (He có 2e, còn lại có 8e), rất trơ về mặt hóa học.
                </p>
              </div>
            </div>
          </div>

          <!-- Section 4: Interactive Periodic Table -->
          <div class="theory-section-block" id="sec4">
            <h3 class="section-title"><i class="fa-solid fa-table-cells"></i> IV. Bảng Tuần Hoàn 20 Nguyên Tố Đầu Tiên (Bấm Để Xem Chi Tiết)</h3>
            <p style="color: var(--text-muted); font-size: 0.9rem;">
              Chú giải màu sắc: <span style="color:#60a5fa;">■ Kim loại</span> | <span style="color:#34d399;">■ Phi kim</span> | <span style="color:#fbbf24;">■ Khí hiếm</span>
            </p>
            <div class="table-responsive">
              <div class="ptable-grid" id="miniPeriodicTable"></div>
            </div>
            <div id="elementDetailCard" class="glass-card" style="padding: 1.2rem 1.6rem; display: none; margin-top: 1rem; border-left: 4px solid var(--accent-cyan);"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. VIEW: VIDEO & 3D SIMULATION -->
    <section class="view-section" id="viewVideo">
      <div class="glass-card" style="padding: 2.2rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:1.5rem;">
          <div>
            <h2 style="font-size: 1.55rem; font-weight: 800; color: #38bdf8; margin-bottom: 4px;">
              <i class="fa-solid fa-photo-film"></i> Thư Viện Video Bài Giảng & Mô Phỏng Nguyên Tử
            </h2>
            <p style="color: var(--text-muted); font-size:0.92rem;">
              Tổng hợp bài giảng trực tuyến chính khóa KHTN 7 theo chuẩn các bộ sách Kết nối tri thức, Chân trời sáng tạo, Cánh diều
            </p>
          </div>
          <div style="display:flex; gap:8px;">
            <a href="https://www.youtube.com/results?search_query=KHTN+7+b%C3%A0i+4+b%E1%BA%A3ng+tu%E1%BA%A7n+ho%C3%A0n" target="_blank" rel="noopener" class="btn-gradient" style="width:auto; padding:8px 16px; font-size:0.85rem; text-decoration:none;">
              <i class="fa-brands fa-youtube" style="color:#ef4444;"></i> Tìm Thêm Video Trên YouTube
            </a>
          </div>
        </div>

        <!-- Verified Video Channels Grid -->
        <div class="video-grid">
          <!-- Card 1: Kết nối tri thức -->
          <div class="video-card glass-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
              <h4 style="color: #e2e8f0; font-size:1rem; font-weight:700;">
                <i class="fa-brands fa-youtube" style="color: #ef4444;"></i> Video 1: Bài Giảng Kết Nối Tri Thức
              </h4>
              <span style="font-size:0.75rem; color:#38bdf8; background:rgba(6,182,212,0.15); padding:2px 8px; border-radius:12px; border:1px solid rgba(6,182,212,0.3);">SGK KNTT</span>
            </div>
            
            <a href="https://www.youtube.com/results?search_query=KHTN+7+B%C3%A0i+4+b%E1%BA%A3ng+tu%E1%BA%A7n+ho%C3%A0n+K%E1%BA%BFt+n%E1%BB%91i+tri+th%E1%BB%A9c" target="_blank" rel="noopener" class="video-preview-box" style="text-decoration:none; display:block;">
              <div class="video-thumb-overlay" style="background: linear-gradient(135deg, rgba(6,182,212,0.2) 0%, rgba(15,23,42,0.95) 80%);">
                <div class="play-btn-circle">
                  <i class="fa-solid fa-play"></i>
                </div>
                <div class="thumb-title">Bài Giảng: Bảng Tuần Hoàn (KNTT)</div>
                <div class="thumb-sub">Mở danh sách bài giảng VietJack & Thầy Nguyễn Chí Sơn trên YouTube</div>
              </div>
            </a>

            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.85rem;">
              <p style="font-size: 0.83rem; color: var(--text-muted); line-height:1.4; margin:0;">
                <i class="fa-solid fa-circle-check" style="color:#10b981;"></i> Đầy đủ lý thuyết & bài tập SGK
              </p>
              <a href="https://www.youtube.com/results?search_query=KHTN+7+B%C3%A0i+4+b%E1%BA%A3ng+tu%E1%BA%A7n+ho%C3%A0n+K%E1%BA%BFt+n%E1%BB%91i+tri+th%E1%BB%A9c" target="_blank" rel="noopener" class="btn-gradient" style="width:auto; padding:7px 16px; font-size:0.82rem; text-decoration:none;">
                <i class="fa-solid fa-arrow-up-right-from-square"></i> Xem Video
              </a>
            </div>
          </div>

          <!-- Card 2: Chân trời sáng tạo -->
          <div class="video-card glass-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
              <h4 style="color: #e2e8f0; font-size:1rem; font-weight:700;">
                <i class="fa-brands fa-youtube" style="color: #ef4444;"></i> Video 2: Bài Giảng Chân Trời Sáng Tạo
              </h4>
              <span style="font-size:0.75rem; color:#a855f7; background:rgba(168,85,247,0.15); padding:2px 8px; border-radius:12px; border:1px solid rgba(168,85,247,0.3);">SGK CTST</span>
            </div>
            
            <a href="https://www.youtube.com/results?search_query=KHTN+7+B%C3%A0i+4+b%E1%BA%A3ng+tu%E1%BA%A7n+ho%C3%A0n+Ch%C3%A2n+tr%E1%BB%9Di+s%C3%A1ng+t%E1%BA%A1o" target="_blank" rel="noopener" class="video-preview-box" style="text-decoration:none; display:block;">
              <div class="video-thumb-overlay" style="background: linear-gradient(135deg, rgba(168,85,247,0.2) 0%, rgba(15,23,42,0.95) 80%);">
                <div class="play-btn-circle" style="background: linear-gradient(135deg, #a855f7, #06b6d4); box-shadow:0 0 25px rgba(168,85,247,0.5);">
                  <i class="fa-solid fa-play"></i>
                </div>
                <div class="thumb-title">Bài Giảng: Bảng Tuần Hoàn (CTST)</div>
                <div class="thumb-sub">Mở bài giảng chi tiết Thầy Cao Cự Giác & OLM trên YouTube</div>
              </div>
            </a>

            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.85rem;">
              <p style="font-size: 0.83rem; color: var(--text-muted); line-height:1.4; margin:0;">
                <i class="fa-solid fa-circle-check" style="color:#10b981;"></i> Trực quan, dễ nhớ quy luật nhóm/chu kỳ
              </p>
              <a href="https://www.youtube.com/results?search_query=KHTN+7+B%C3%A0i+4+b%E1%BA%A3ng+tu%E1%BA%A7n+ho%C3%A0n+Ch%C3%A2n+tr%E1%BB%9Di+s%C3%A1ng+t%E1%BA%A1o" target="_blank" rel="noopener" class="btn-gradient" style="width:auto; padding:7px 16px; font-size:0.82rem; text-decoration:none; background: linear-gradient(135deg, #a855f7, #06b6d4);">
                <i class="fa-solid fa-arrow-up-right-from-square"></i> Xem Video
              </a>
            </div>
          </div>

          <!-- Card 3: Cánh diều -->
          <div class="video-card glass-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
              <h4 style="color: #e2e8f0; font-size:1rem; font-weight:700;">
                <i class="fa-brands fa-youtube" style="color: #ef4444;"></i> Video 3: Bài Giảng Bộ Sách Cánh Diều
              </h4>
              <span style="font-size:0.75rem; color:#f59e0b; background:rgba(245,158,11,0.15); padding:2px 8px; border-radius:12px; border:1px solid rgba(245,158,11,0.3);">SGK Cánh Diều</span>
            </div>
            
            <a href="https://www.youtube.com/results?search_query=KHTN+7+B%C3%A0i+3+S%C6%A1+l%C6%B0%E1%BB%A3c+b%E1%BA%A3ng+tu%E1%BA%A7n+ho%C3%A0n+C%C3%A1nh+di%E1%BB%81u" target="_blank" rel="noopener" class="video-preview-box" style="text-decoration:none; display:block;">
              <div class="video-thumb-overlay" style="background: linear-gradient(135deg, rgba(245,158,11,0.2) 0%, rgba(15,23,42,0.95) 80%);">
                <div class="play-btn-circle" style="background: linear-gradient(135deg, #f59e0b, #ef4444); box-shadow:0 0 25px rgba(245,158,11,0.5);">
                  <i class="fa-solid fa-play"></i>
                </div>
                <div class="thumb-title">Bài Giảng: Bảng Tuần Hoàn (Cánh Diều)</div>
                <div class="thumb-sub">Mở danh sách bài giảng Tech12h & VietJack Cánh Diều</div>
              </div>
            </a>

            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.85rem;">
              <p style="font-size: 0.83rem; color: var(--text-muted); line-height:1.4; margin:0;">
                <i class="fa-solid fa-circle-check" style="color:#10b981;"></i> Trọng tâm ô nguyên tố & phân loại kim loại
              </p>
              <a href="https://www.youtube.com/results?search_query=KHTN+7+B%C3%A0i+3+S%C6%A1+l%C6%B0%E1%BB%A3c+b%E1%BA%A3ng+tu%E1%BA%A7n+ho%C3%A0n+C%C3%A1nh+di%E1%BB%81u" target="_blank" rel="noopener" class="btn-gradient" style="width:auto; padding:7px 16px; font-size:0.82rem; text-decoration:none; background: linear-gradient(135deg, #f59e0b, #ef4444);">
                <i class="fa-solid fa-arrow-up-right-from-square"></i> Xem Video
              </a>
            </div>
          </div>
        </div>

        <!-- Interactive 3D Atom Simulation Canvas -->
        <div class="atom-sim-wrapper" style="margin-top:2.2rem;">
          <h3 style="color: #f1f5f9; margin-bottom: 0.5rem; font-size:1.3rem;">
            <i class="fa-solid fa-atom fa-spin" style="--fa-animation-duration: 6s; color: var(--accent-cyan);"></i> 
            Mô Phỏng Trực Quan Quỹ Đạo Electron Nguyên Tử (Live 3D Canvas)
          </h3>
          <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom:1rem;">
            Bấm chọn các nguyên tố dưới đây để quan sát sự phân bố electron trên các lớp theo mô hình Rutherford - Bohr:
          </p>

          <div class="sim-controls">
            <button type="button" class="sim-btn active" data-sym="H" onclick="setSimElement('H')">1. Hydrogen (1e, 1 lớp)</button>
            <button type="button" class="sim-btn" data-sym="He" onclick="setSimElement('He')">2. Helium (2e, 1 lớp)</button>
            <button type="button" class="sim-btn" data-sym="C" onclick="setSimElement('C')">6. Carbon (6e, 2 lớp)</button>
            <button type="button" class="sim-btn" data-sym="O" onclick="setSimElement('O')">8. Oxygen (8e, 2 lớp)</button>
            <button type="button" class="sim-btn" data-sym="Na" onclick="setSimElement('Na')">11. Sodium (11e, 3 lớp)</button>
            <button type="button" class="sim-btn" data-sym="Cl" onclick="setSimElement('Cl')">17. Chlorine (17e, 3 lớp)</button>
          </div>

          <div style="margin-top: 1.5rem; display: flex; justify-content: center;">
            <canvas id="atomCanvas" width="500" height="400"></canvas>
          </div>
          <div id="atomSimInfo" style="margin-top: 0.75rem; font-weight: 600; color: #38bdf8;">
            Đang hiển thị nguyên tố: Hydrogen (Z = 1) - 1 electron ở lớp 1
          </div>
        </div>
      </div>
    </section>

    <!-- 4. VIEW: QUIZ PRACTICE (50 CÂU HỎI CHIA 5 DẠNG) -->
    <section class="view-section" id="viewQuiz">
      <div class="quiz-layout">
        <div class="quiz-meta-bar glass-card">
          <div class="quiz-progress-wrap">
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 600;">
              <span>Câu hỏi <strong id="currentQNum">1</strong> / <strong id="totalQNum">50</strong></span>
              <span id="progressPercent">2% Hoàn thành</span>
            </div>
            <div class="progress-bar-bg">
              <div class="progress-bar-fill" id="progressBarFill"></div>
            </div>
          </div>
          <div class="score-badge">
            <i class="fa-solid fa-star"></i>
            <span>Điểm: <span id="currentScore">0</span></span>
          </div>
        </div>

        <div class="quiz-filters">
          <button class="filter-btn active" onclick="filterQuizCategory('all')">Tất cả (50 câu)</button>
          <button class="filter-btn" onclick="filterQuizCategory('choice')">1. Nhiều lựa chọn (10)</button>
          <button class="filter-btn" onclick="filterQuizCategory('fill')">2. Điền khuyết (10)</button>
          <button class="filter-btn" onclick="filterQuizCategory('match')">3. Ghép cột (10)</button>
          <button class="filter-btn" onclick="filterQuizCategory('tf')">4. Đúng / Sai (10)</button>
          <button class="filter-btn" onclick="filterQuizCategory('essay')">5. Tự luận ngắn (10)</button>
        </div>

        <div class="question-box glass-card" id="questionContainer">
          <div class="q-type-badge" id="qTypeBadge">Trắc nghiệm</div>
          <h3 class="q-title" id="qTitle">Đang tải câu hỏi...</h3>

          <div id="interactiveArea"></div>

          <div class="explanation-box" id="explanationBox">
            <div class="exp-title">
              <i class="fa-solid fa-circle-info"></i> Giải Thích Chi Tiết Sách Giáo Khoa:
            </div>
            <div class="exp-text" id="explanationText"></div>
          </div>
        </div>

        <div class="quiz-nav-actions">
          <button class="btn-secondary" id="btnPrevQ" onclick="navigateQuestion(-1)">
            <i class="fa-solid fa-arrow-left"></i> Câu Trước
          </button>
          <button class="btn-gradient" id="btnNextQ" onclick="navigateQuestion(1)" style="width: auto; padding: 10px 24px;">
            <span>Câu Tiếp Theo</span> <i class="fa-solid fa-arrow-right"></i>
          </button>
        </div>
      </div>
    </section>

    <!-- 5. VIEW: RESULT & REPORT EXPORT -->
    <section class="view-section" id="viewResult">
      <div class="result-wrapper glass-card" id="reportCardArea">
        <div class="result-header-icon">
          <i class="fa-solid fa-award"></i>
        </div>
        <h2 style="font-size: 1.8rem; font-weight: 800; margin-bottom: 0.3rem;">KẾT QUẢ HỌC TẬP</h2>
        <p style="color: var(--text-muted); font-size: 0.95rem;">
          Học sinh: <strong id="resStudentName" style="color:#fff;">Nguyễn Văn A</strong> | Lớp: <strong id="resStudentClass" style="color:#fff;">7A</strong>
        </p>

        <div class="result-score-circle" id="resFinalScore">80/100</div>
        <p id="resEvaluation" style="font-size: 1.1rem; font-weight: 600; color: #34d399; margin-bottom: 1.5rem;">
          Xuất sắc! Em đã nắm rất vững kiến thức bảng tuần hoàn.
        </p>

        <div class="result-stats-grid">
          <div class="stat-pill">
            <div class="stat-val" id="statCorrectCount">40</div>
            <div class="stat-lbl">Câu Trả Lời Đúng</div>
          </div>
          <div class="stat-pill">
            <div class="stat-val" id="statAccuracy">80%</div>
            <div class="stat-lbl">Tỉ Lệ Chính Xác</div>
          </div>
          <div class="stat-pill">
            <div class="stat-val" id="statCompleted">50/50</div>
            <div class="stat-lbl">Số Câu Hoàn Thành</div>
          </div>
        </div>

        <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-top: 2rem;">
          <button class="btn-gradient" onclick="exportResultImage()" style="width: auto; padding: 12px 24px;">
            <i class="fa-solid fa-download"></i> Tải Báo Cáo Kết Quả (Ảnh)
          </button>
          <button class="btn-secondary" onclick="restartQuiz()">
            <i class="fa-solid fa-rotate-left"></i> Làm Lại Bài Kiểm Tra
          </button>
        </div>
      </div>
    </section>

    <!-- 6. VIEW: LEADERBOARD -->
    <section class="view-section" id="viewLeaderboard">
      <div class="glass-card" style="max-width: 650px; margin: 2rem auto; padding: 2rem;">
        <div style="text-align: center; margin-bottom: 1.5rem;">
          <div style="font-size: 2.5rem; color: #fbbf24; margin-bottom: 0.5rem;">
            <i class="fa-solid fa-trophy"></i>
          </div>
          <h2 style="font-size: 1.6rem; font-weight: 800;">BẢNG VINH DANH HỌC TẬP</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">
            Top 5 Học sinh đạt điểm cao nhất (Lưu trên máy LocalStorage)
          </p>
        </div>

        <div class="leaderboard-box" id="leaderboardList"></div>

        <div style="text-align: center; margin-top: 1.5rem; display: flex; justify-content: center; gap: 12px;">
          <button class="btn-secondary" onclick="clearLeaderboardData()">
            <i class="fa-solid fa-trash-can"></i> Xóa Dữ Liệu Xếp Hạng
          </button>
        </div>
      </div>
    </section>

  </main>

  <script>
"""

html_tail = """
    // Google Apps Script Live Web App URL
    const APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbynefdy9sF4YOx3ZhFkI7-kkMdm8KpXG8Cd8OGqYPWh6XGVr_BMqa-19UwgJ4kQ70TL/exec";

    // 20 First Elements for Interactive Periodic Table
    const ELEMENTS_20 = [
      { z: 1, sym: "H", name: "Hydrogen", mass: 1.008, type: "nonmetal", period: 1, group: "IA", shells: [1] },
      { z: 2, sym: "He", name: "Helium", mass: 4.003, type: "noble", period: 1, group: "VIIIA", shells: [2] },
      { z: 3, sym: "Li", name: "Lithium", mass: 6.941, type: "metal", period: 2, group: "IA", shells: [2, 1] },
      { z: 4, sym: "Be", name: "Beryllium", mass: 9.012, type: "metal", period: 2, group: "IIA", shells: [2, 2] },
      { z: 5, sym: "B", name: "Boron", mass: 10.81, type: "nonmetal", period: 2, group: "IIIA", shells: [2, 3] },
      { z: 6, sym: "C", name: "Carbon", mass: 12.011, type: "nonmetal", period: 2, group: "IVA", shells: [2, 4] },
      { z: 7, sym: "N", name: "Nitrogen", mass: 14.007, type: "nonmetal", period: 2, group: "VA", shells: [2, 5] },
      { z: 8, sym: "O", name: "Oxygen", mass: 15.999, type: "nonmetal", period: 2, group: "VIA", shells: [2, 6] },
      { z: 9, sym: "F", name: "Fluorine", mass: 18.998, type: "nonmetal", period: 2, group: "VIIA", shells: [2, 7] },
      { z: 10, sym: "Ne", name: "Neon", mass: 20.180, type: "noble", period: 2, group: "VIIIA", shells: [2, 8] },
      { z: 11, sym: "Na", name: "Sodium", mass: 22.990, type: "metal", period: 3, group: "IA", shells: [2, 8, 1] },
      { z: 12, sym: "Mg", name: "Magnesium", mass: 24.305, type: "metal", period: 3, group: "IIA", shells: [2, 8, 2] },
      { z: 13, sym: "Al", name: "Aluminium", mass: 26.982, type: "metal", period: 3, group: "IIIA", shells: [2, 8, 3] },
      { z: 14, sym: "Si", name: "Silicon", mass: 28.085, type: "nonmetal", period: 3, group: "IVA", shells: [2, 8, 4] },
      { z: 15, sym: "P", name: "Phosphorus", mass: 30.974, type: "nonmetal", period: 3, group: "VA", shells: [2, 8, 5] },
      { z: 16, sym: "S", name: "Sulfur", mass: 32.065, type: "nonmetal", period: 3, group: "VIA", shells: [2, 8, 6] },
      { z: 17, sym: "Cl", name: "Chlorine", mass: 35.453, type: "nonmetal", period: 3, group: "VIIA", shells: [2, 8, 7] },
      { z: 18, sym: "Ar", name: "Argon", mass: 39.948, type: "noble", period: 3, group: "VIIIA", shells: [2, 8, 8] },
      { z: 19, sym: "K", name: "Potassium", mass: 39.098, type: "metal", period: 4, group: "IA", shells: [2, 8, 8, 1] },
      { z: 20, sym: "Ca", name: "Calcium", mass: 40.078, type: "metal", period: 4, group: "IIA", shells: [2, 8, 8, 2] }
    ];

    // =========================================================================
    // 2. WEB AUDIO API: TẠO ÂM THANH THỦ CÔNG
    // =========================================================================
    let audioCtx = null;
    function getAudioContext() {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
      return audioCtx;
    }

    function playCorrectSound() {
      try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        
        const osc1 = ctx.createOscillator();
        const gain1 = ctx.createGain();
        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(587.33, now);
        gain1.gain.setValueAtTime(0.15, now);
        gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
        osc1.connect(gain1);
        gain1.connect(ctx.destination);
        osc1.start(now);
        osc1.stop(now + 0.3);

        const osc2 = ctx.createOscillator();
        const gain2 = ctx.createGain();
        osc2.type = 'sine';
        osc2.frequency.setValueAtTime(880, now + 0.12);
        gain2.gain.setValueAtTime(0.2, now + 0.12);
        gain2.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
        osc2.connect(gain2);
        gain2.connect(ctx.destination);
        osc2.start(now + 0.12);
        osc2.stop(now + 0.5);
      } catch (e) {
        console.warn('Audio play failed:', e);
      }
    }

    function playWrongSound() {
      try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(140, now);
        osc.frequency.linearRampToValueAtTime(90, now + 0.35);
        gain.gain.setValueAtTime(0.25, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.35);
      } catch (e) {
        console.warn('Audio play failed:', e);
      }
    }

    // =========================================================================
    // 3. CORE STATE & USER SESSION (AN TOÀN TRÊN MỌI MÔI TRƯỜNG & IFRAME)
    // =========================================================================
    const safeStorage = {
      _mem: {},
      getItem(k) {
        try {
          if (typeof window !== 'undefined' && window.localStorage) {
            return window.localStorage.getItem(k);
          }
        } catch (e) {}
        try {
          if (typeof window !== 'undefined' && window.sessionStorage) {
            return window.sessionStorage.getItem(k);
          }
        } catch (e) {}
        return this._mem[k] || null;
      },
      setItem(k, v) {
        try {
          if (typeof window !== 'undefined' && window.localStorage) {
            window.localStorage.setItem(k, v);
          }
        } catch (e) {}
        try {
          if (typeof window !== 'undefined' && window.sessionStorage) {
            window.sessionStorage.setItem(k, v);
          }
        } catch (e) {}
        this._mem[k] = String(v);
      },
      removeItem(k) {
        try {
          if (typeof window !== 'undefined' && window.localStorage) {
            window.localStorage.removeItem(k);
          }
        } catch (e) {}
        try {
          if (typeof window !== 'undefined' && window.sessionStorage) {
            window.sessionStorage.removeItem(k);
          }
        } catch (e) {}
        delete this._mem[k];
      }
    };

    let currentUser = {
      name: safeStorage.getItem('khtn7_user_name') || '',
      className: safeStorage.getItem('khtn7_user_class') || ''
    };

    let isLoggedIn = !!(currentUser.name && currentUser.className);

    let activeFilter = 'all';
    let filteredQuestions = [...QUIZ_DATA];
    let currentIndex = 0;
    let userAnswers = {};
    let score = 0;

    let selectedLeftMatch = null;
    let selectedRightMatch = null;
    let activeMatchedPairs = {};

    document.addEventListener('DOMContentLoaded', () => {
      try { renderPeriodicMiniTable(); } catch (e) { console.warn(e); }
      try { initAtomSimulator(); } catch (e) { console.warn(e); }
      try { renderLeaderboard(); } catch (e) { console.warn(e); }
      try { loadQuestion(); } catch (e) { console.warn(e); }

      // Gắn sự kiện phím Enter cho ô nhập tên & lớp
      const nameInp = document.getElementById('inputStudentName');
      const classInp = document.getElementById('inputStudentClass');
      if (nameInp) {
        nameInp.addEventListener('keydown', (e) => {
          if (e.key === 'Enter') {
            e.preventDefault();
            if (classInp && !classInp.value.trim()) {
              classInp.focus();
            } else {
              handleLoginSubmit(e);
            }
          }
        });
      }
      if (classInp) {
        classInp.addEventListener('keydown', (e) => {
          if (e.key === 'Enter') {
            e.preventDefault();
            handleLoginSubmit(e);
          }
        });
      }

      if (isLoggedIn) {
        initUserBadge();
        switchView('theory');
      } else {
        initUserBadge();
        switchView('login');
        showLoginAlert(false);
      }
    });

    function initUserBadge() {
      const letter = document.getElementById('avatarLetter');
      const nameTxt = document.getElementById('userNameDisplay');
      const logoutBtn = document.getElementById('btnLogout');

      if (isLoggedIn && currentUser.name) {
        letter.textContent = currentUser.name.trim().charAt(0).toUpperCase();
        nameTxt.textContent = `${currentUser.name} (${currentUser.className})`;
        if (logoutBtn) logoutBtn.style.display = 'inline-flex';
      } else {
        letter.textContent = '?';
        nameTxt.textContent = 'Đăng nhập';
        if (logoutBtn) logoutBtn.style.display = 'none';
      }
    }

    function copyAppShareLink() {
      const url = APPS_SCRIPT_URL || window.location.href;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(() => {
          alert('Đã sao chép liên kết Web App thành công!\n' + url);
        }).catch(() => {
          prompt('Sao chép đường link ứng dụng tại đây:', url);
        });
      } else {
        prompt('Sao chép đường link ứng dụng tại đây:', url);
      }
    }

    function handleLogout() {
      if (confirm(`Em có chắc chắn muốn đăng xuất tài khoản "${currentUser.name || 'này'}"?`)) {
        safeStorage.removeItem('khtn7_user_name');
        safeStorage.removeItem('khtn7_user_class');
        currentUser = { name: '', className: '' };
        isLoggedIn = false;
        userAnswers = {};
        score = 0;
        currentIndex = 0;

        const inpName = document.getElementById('inputStudentName');
        const inpClass = document.getElementById('inputStudentClass');
        if (inpName) inpName.value = '';
        if (inpClass) inpClass.value = '';

        initUserBadge();
        showLoginAlert(false);
        switchView('login');
      }
    }

    function showLoginModal() {
      switchView('login');
      if (currentUser.name) {
        document.getElementById('inputStudentName').value = currentUser.name;
        document.getElementById('inputStudentClass').value = currentUser.className;
      }
    }

    function showLoginAlert(show = true) {
      const alertBox = document.getElementById('loginAlert');
      if (alertBox) {
        alertBox.style.display = show ? 'flex' : 'none';
        if (show) triggerScreenShake();
      }
    }

    function handleLoginSubmit(e) {
      if (e) {
        if (typeof e.preventDefault === 'function') e.preventDefault();
        if (typeof e.stopPropagation === 'function') e.stopPropagation();
      }
      try {
        const nameInput = document.getElementById('inputStudentName');
        const classInput = document.getElementById('inputStudentClass');
        const name = nameInput ? nameInput.value.trim() : '';
        const cls = classInput ? classInput.value.trim() : '';

        if (!name || !cls) {
          showLoginAlert(true);
          return false;
        }

        currentUser.name = name;
        currentUser.className = cls;
        isLoggedIn = true;

        safeStorage.setItem('khtn7_user_name', name);
        safeStorage.setItem('khtn7_user_class', cls);

        initUserBadge();
        try { triggerConfetti(); } catch (err) {}
        showLoginAlert(false);
        switchView('theory');
        return false;
      } catch (err) {
        console.error("Login submit error:", err);
        isLoggedIn = true;
        switchView('theory');
        return false;
      }
    }

    function handleBrandClick() {
      if (isLoggedIn) {
        switchView('theory');
      } else {
        switchView('login');
      }
    }

    function switchView(viewName) {
      // Bắt buộc đăng nhập: Nếu chưa đăng nhập và muốn vào màn hình khác -> chặn và chuyển về login
      if (!isLoggedIn && viewName !== 'login') {
        showLoginAlert(true);
        switchView('login');
        return;
      }

      const views = ['theory', 'video', 'quiz', 'result', 'leaderboard', 'login'];
      views.forEach(v => {
        const el = document.getElementById('view' + v.charAt(0).toUpperCase() + v.slice(1));
        if (el) el.classList.remove('active');
        const tab = document.getElementById('tab' + v.charAt(0).toUpperCase() + v.slice(1));
        if (tab) tab.classList.remove('active');
      });

      const activeEl = document.getElementById('view' + viewName.charAt(0).toUpperCase() + viewName.slice(1));
      if (activeEl) activeEl.classList.add('active');
      const activeTab = document.getElementById('tab' + viewName.charAt(0).toUpperCase() + viewName.slice(1));
      if (activeTab) activeTab.classList.add('active');

      if (viewName === 'leaderboard') {
        renderLeaderboard();
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // =========================================================================
    // 4. PERIODIC TABLE & ATOM SIMULATOR
    // =========================================================================
    function renderPeriodicMiniTable() {
      const grid = document.getElementById('miniPeriodicTable');
      if (!grid) return;
      grid.innerHTML = '';

      const posMap = {
        1: [1, 1], 2: [1, 18],
        3: [2, 1], 4: [2, 2], 5: [2, 13], 6: [2, 14], 7: [2, 15], 8: [2, 16], 9: [2, 17], 10: [2, 18],
        11: [3, 1], 12: [3, 2], 13: [3, 13], 14: [3, 14], 15: [3, 15], 16: [3, 16], 17: [3, 17], 18: [3, 18],
        19: [4, 1], 20: [4, 2]
      };

      for (let r = 1; r <= 4; r++) {
        for (let c = 1; c <= 18; c++) {
          let found = null;
          for (let z in posMap) {
            if (posMap[z][0] === r && posMap[z][1] === c) {
              found = ELEMENTS_20.find(item => item.z == z);
              break;
            }
          }

          if (found) {
            const cell = document.createElement('div');
            let colorCls = found.type === 'metal' ? 'p-metal' : (found.type === 'noble' ? 'p-noble' : 'p-nonmetal');
            cell.className = `p-cell ${colorCls}`;
            cell.innerHTML = `<span class="p-num">${found.z}</span><span class="p-sym">${found.sym}</span>`;
            cell.onclick = () => showElementDetail(found);
            grid.appendChild(cell);
          } else {
            const empty = document.createElement('div');
            empty.className = 'p-cell p-empty';
            grid.appendChild(empty);
          }
        }
      }
    }

    function showElementDetail(elm) {
      const box = document.getElementById('elementDetailCard');
      const typeLabel = elm.type === 'metal' ? 'Kim loại' : (elm.type === 'noble' ? 'Khí hiếm' : 'Phi kim');
      box.style.display = 'block';
      box.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
          <div>
            <h4 style="font-size:1.2rem; color:#fff;">Ô số ${elm.z}: ${elm.name} (${elm.sym})</h4>
            <p style="color:var(--text-muted); font-size:0.9rem;">
              • Khối lượng: <strong>${elm.mass} amu</strong> | Phân loại: <strong style="color:var(--accent-cyan);">${typeLabel}</strong>
            </p>
            <p style="color:#cbd5e1; font-size:0.85rem; margin-top:4px;">
              • Vị trí: <strong>Chu kỳ ${elm.period}</strong> (có ${elm.shells.length} lớp e), <strong>Nhóm ${elm.group}</strong> (${elm.shells[elm.shells.length - 1]} electron ngoài cùng).
            </p>
          </div>
          <button class="sim-btn" onclick="setSimElement('${elm.sym}'); switchView('video');" style="background:var(--accent-cyan); color:#0f172a; font-weight:700;">
            <i class="fa-solid fa-atom"></i> Xem Mô Phỏng 3D
          </button>
        </div>
      `;
      box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    let simTarget = ELEMENTS_20[0];
    let animAngle = 0;
    let simAnimId = null;

    function initAtomSimulator() {
      const canvas = document.getElementById('atomCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');

      // Huy bo vong lap cu neu co de chong trung lap frame gay giat
      if (simAnimId) {
        cancelAnimationFrame(simAnimId);
        simAnimId = null;
      }

      function drawSim() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;

        // 1. Hat nhan (Proton & Neutron)
        // Vung sang hat nhan
        ctx.beginPath();
        ctx.arc(centerX, centerY, 30, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(244, 63, 94, 0.2)';
        ctx.fill();

        // Hat nhan chinh
        ctx.beginPath();
        ctx.arc(centerX, centerY, 22, 0, Math.PI * 2);
        const grad = ctx.createRadialGradient(centerX - 4, centerY - 4, 3, centerX, centerY, 22);
        grad.addColorStop(0, '#fb7185');
        grad.addColorStop(1, '#9f1239');
        ctx.fillStyle = grad;
        ctx.fill();

        // Chu so proton trong hat nhan
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 13px "Be Vietnam Pro", sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(`+${simTarget.z}`, centerX, centerY);

        // 2. Cac quy dao & electron quay muot ma
        const shellRadii = [60, 105, 150, 185];
        simTarget.shells.forEach((electronCount, shellIdx) => {
          const r = shellRadii[shellIdx];

          // Duong quy dao elip / tron
          ctx.beginPath();
          ctx.arc(centerX, centerY, r, 0, Math.PI * 2);
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.18)';
          ctx.setLineDash([5, 5]);
          ctx.lineWidth = 1.5;
          ctx.stroke();
          ctx.setLineDash([]);

          // Toc do quay hai hoa (lop trong nhanh nhe, lop ngoai quay cham tinh te)
          const speedMultiplier = 1.0 - (shellIdx * 0.18);
          for (let e = 0; e < electronCount; e++) {
            const theta = (animAngle * speedMultiplier) + (e * 2 * Math.PI / electronCount);
            const ex = centerX + r * Math.cos(theta);
            const ey = centerY + r * Math.sin(theta);

            // Vien quang sang electron (thay the shadowBlur cuc ky tiet kiem GPU)
            ctx.beginPath();
            ctx.arc(ex, ey, 9, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(6, 182, 212, 0.28)';
            ctx.fill();

            // Hat electron chinh
            ctx.beginPath();
            ctx.arc(ex, ey, 5.5, 0, Math.PI * 2);
            ctx.fillStyle = '#06b6d4';
            ctx.fill();

            // Diem sang loi electron tao cam giac 3D
            ctx.beginPath();
            ctx.arc(ex - 1.5, ey - 1.5, 2, 0, Math.PI * 2);
            ctx.fillStyle = '#ffffff';
            ctx.fill();
          }
        });

        // Tang goc quay muot ma
        animAngle += 0.009;
        simAnimId = requestAnimationFrame(drawSim);
      }

      drawSim();
    }

    function setSimElement(symbol) {
      const elm = ELEMENTS_20.find(e => e.sym === symbol);
      if (!elm) return;
      simTarget = elm;

      const info = document.getElementById('atomSimInfo');
      if (info) {
        info.innerHTML = `<span style="color:#38bdf8; font-weight:700;">${elm.name} (${elm.sym})</span> &nbsp;•&nbsp; Điện tích hạt nhân: <strong>+${elm.z}</strong> &nbsp;•&nbsp; ${elm.shells.length} lớp electron: <strong>[${elm.shells.join(', ')}]</strong>`;
      }

      // Cap nhat active class chinh xac duy nhat 1 nut duoc chon
      document.querySelectorAll('.sim-controls .sim-btn').forEach(b => {
        const isSelected = b.getAttribute('data-sym') === symbol;
        b.classList.toggle('active', isSelected);
      });
    }

    // =========================================================================
    // 5. QUIZ LOGIC
    // =========================================================================
    function filterQuizCategory(cat) {
      activeFilter = cat;
      document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('onclick').includes(cat));
      });

      if (cat === 'all') {
        filteredQuestions = [...QUIZ_DATA];
      } else {
        filteredQuestions = QUIZ_DATA.filter(q => q.type === cat);
      }
      currentIndex = 0;
      loadQuestion();
    }

    function loadQuestion() {
      if (filteredQuestions.length === 0) return;
      const q = filteredQuestions[currentIndex];
      const qId = q.id;

      document.getElementById('currentQNum').textContent = currentIndex + 1;
      document.getElementById('totalQNum').textContent = filteredQuestions.length;
      const percent = Math.round(((currentIndex + 1) / filteredQuestions.length) * 100);
      document.getElementById('progressPercent').textContent = `${percent}% Hoàn thành`;
      document.getElementById('progressBarFill').style.width = `${percent}%`;
      document.getElementById('currentScore').textContent = score;

      document.getElementById('qTypeBadge').textContent = q.category;
      document.getElementById('qTitle').textContent = `Câu ${q.id}: ${q.question}`;

      const container = document.getElementById('interactiveArea');
      container.innerHTML = '';

      const expBox = document.getElementById('explanationBox');
      const expText = document.getElementById('explanationText');
      expBox.classList.remove('show');
      expText.textContent = q.explanation;

      const state = userAnswers[qId];

      if (q.type === 'choice' || q.type === 'tf') {
        renderChoiceQuestion(q, container, state);
      } else if (q.type === 'fill') {
        renderFillQuestion(q, container, state);
      } else if (q.type === 'match') {
        renderMatchQuestion(q, container, state);
      } else if (q.type === 'essay') {
        renderEssayQuestion(q, container, state);
      }

      if (state && state.answered) {
        expBox.classList.add('show');
      }

      document.getElementById('btnPrevQ').disabled = (currentIndex === 0);
      const isLast = (currentIndex === filteredQuestions.length - 1);
      const nextBtnSpan = document.getElementById('btnNextQ').querySelector('span');
      if (isLast) {
        nextBtnSpan.textContent = "Xem Kết Quả Tổng Kết";
      } else {
        nextBtnSpan.textContent = "Câu Tiếp Theo";
      }
    }

    function renderChoiceQuestion(q, container, state) {
      const grid = document.createElement('div');
      grid.className = 'options-grid';
      const prefixes = ['A', 'B', 'C', 'D'];

      q.options.forEach((opt, idx) => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.innerHTML = `<span class="opt-prefix">${prefixes[idx] || (idx+1)}</span> <span>${opt}</span>`;

        if (state && state.answered) {
          btn.disabled = true;
          if (idx === q.answer) btn.classList.add('correct');
          if (state.selected === idx && idx !== q.answer) btn.classList.add('wrong');
        } else {
          btn.onclick = () => submitChoiceAnswer(q, idx);
        }
        grid.appendChild(btn);
      });
      container.appendChild(grid);
    }

    function submitChoiceAnswer(q, selectedIdx) {
      const isCorrect = (selectedIdx === q.answer);
      handleAnswerResult(q, isCorrect, selectedIdx);
    }

    function renderFillQuestion(q, container, state) {
      const wrap = document.createElement('div');
      wrap.innerHTML = `
        <div style="font-size:0.85rem; color:var(--accent-cyan); margin-bottom:0.6rem;">${q.blankHint}</div>
        <div class="fill-input-box">
          <input type="text" id="fillInputBox" class="fill-input" placeholder="Gõ câu trả lời vào đây..." ${state && state.answered ? 'disabled' : ''}>
          <button class="btn-gradient" id="btnSubmitFill" style="width:auto; padding:0 24px;" ${state && state.answered ? 'disabled' : ''}>
            <i class="fa-solid fa-check"></i> Trả lời
          </button>
        </div>
      `;
      container.appendChild(wrap);

      const input = wrap.querySelector('#fillInputBox');
      const btn = wrap.querySelector('#btnSubmitFill');

      if (state && state.answered) {
        input.value = state.selected;
        input.style.borderColor = state.isCorrect ? '#10b981' : '#f43f5e';
      } else {
        btn.onclick = () => {
          const val = input.value.trim().toLowerCase();
          if (!val) return;
          const isCorrect = q.acceptable.some(acc => acc.toLowerCase() === val);
          handleAnswerResult(q, isCorrect, input.value.trim());
        };
        input.addEventListener('keypress', (e) => {
          if (e.key === 'Enter') btn.click();
        });
      }
    }

    function renderMatchQuestion(q, container, state) {
      const wrap = document.createElement('div');
      wrap.innerHTML = `
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">
          <i class="fa-solid fa-hand-pointer"></i> Hướng dẫn: Nhấp chọn 1 mục ở Cột A, sau đó nhấp chọn mục tương ứng ở Cột B để ghép đôi.
        </p>
      `;

      const matchCols = document.createElement('div');
      matchCols.className = 'match-columns';

      const colA = document.createElement('div');
      const colB = document.createElement('div');

      const shuffledRights = [...q.pairs.map(p => p.right)].sort(() => 0.5 - Math.random());

      q.pairs.forEach((pair) => {
        const itemA = document.createElement('div');
        itemA.className = 'match-item';
        itemA.dataset.key = pair.left;
        itemA.innerHTML = `<span>${pair.left}</span> <i class="fa-solid fa-arrow-right-long" style="opacity:0.4;"></i>`;
        colA.appendChild(itemA);
      });

      shuffledRights.forEach((rVal) => {
        const itemB = document.createElement('div');
        itemB.className = 'match-item';
        itemB.dataset.val = rVal;
        itemB.innerHTML = `<span>${rVal}</span> <i class="fa-regular fa-circle"></i>`;
        colB.appendChild(itemB);
      });

      matchCols.appendChild(colA);
      matchCols.appendChild(colB);
      wrap.appendChild(matchCols);
      container.appendChild(wrap);

      selectedLeftMatch = null;
      selectedRightMatch = null;
      activeMatchedPairs = state ? (state.selected || {}) : {};

      if (state && state.answered) {
        colA.querySelectorAll('.match-item').forEach(it => it.classList.add('matched'));
        colB.querySelectorAll('.match-item').forEach(it => it.classList.add('matched'));
      } else {
        colA.querySelectorAll('.match-item').forEach(itA => {
          itA.onclick = () => {
            colA.querySelectorAll('.match-item').forEach(i => i.classList.remove('selected'));
            itA.classList.add('selected');
            selectedLeftMatch = itA.dataset.key;
            checkMatchingPair(q, colA, colB);
          };
        });

        colB.querySelectorAll('.match-item').forEach(itB => {
          itB.onclick = () => {
            colB.querySelectorAll('.match-item').forEach(i => i.classList.remove('selected'));
            itB.classList.add('selected');
            selectedRightMatch = itB.dataset.val;
            checkMatchingPair(q, colA, colB);
          };
        });
      }
    }

    function checkMatchingPair(q, colA, colB) {
      if (selectedLeftMatch && selectedRightMatch) {
        activeMatchedPairs[selectedLeftMatch] = selectedRightMatch;

        const elA = colA.querySelector(`[data-key="${selectedLeftMatch}"]`);
        const elB = colB.querySelector(`[data-val="${selectedRightMatch}"]`);
        if (elA) { elA.classList.add('matched'); elA.classList.remove('selected'); }
        if (elB) { elB.classList.add('matched'); elB.classList.remove('selected'); }

        selectedLeftMatch = null;
        selectedRightMatch = null;

        if (Object.keys(activeMatchedPairs).length === q.pairs.length) {
          let correctPairs = 0;
          q.pairs.forEach(p => {
            if (activeMatchedPairs[p.left] === p.right) correctPairs++;
          });
          const isCorrect = (correctPairs === q.pairs.length);
          handleAnswerResult(q, isCorrect, activeMatchedPairs);
        }
      }
    }

    function renderEssayQuestion(q, container, state) {
      const wrap = document.createElement('div');
      wrap.innerHTML = `
        <textarea id="essayInput" class="essay-textarea" placeholder="Nhập câu trả lời ngắn của em theo ý hiểu..." ${state && state.answered ? 'disabled' : ''}></textarea>
        <button class="btn-gradient" id="btnSubmitEssay" style="width:auto; padding:10px 24px;" ${state && state.answered ? 'disabled' : ''}>
          <i class="fa-solid fa-paper-plane"></i> Nộp Bài & Xem Đáp Án Chuẩn
        </button>
        <div id="essayModelBox" style="margin-top:1rem; padding:1.2rem; background:rgba(6,182,212,0.1); border-radius:10px; border:1px solid var(--accent-cyan); display:${state && state.answered ? 'block' : 'none'};">
          <h5 style="color:var(--accent-cyan); margin-bottom:6px;"><i class="fa-solid fa-graduation-cap"></i> Gợi ý đáp án chuẩn:</h5>
          <p style="color:#e2e8f0; font-size:0.9rem; line-height:1.6; white-space:pre-line;">${q.modelAnswer}</p>
        </div>
      `;
      container.appendChild(wrap);

      const area = wrap.querySelector('#essayInput');
      const btn = wrap.querySelector('#btnSubmitEssay');
      const modelBox = wrap.querySelector('#essayModelBox');

      if (state && state.answered) {
        area.value = state.selected;
      } else {
        btn.onclick = () => {
          const txt = area.value.trim().toLowerCase();
          if (!txt) {
            alert('Vui lòng gõ nội dung câu trả lời trước khi nộp bài!');
            return;
          }
          let hitCount = 0;
          q.keywords.forEach(kw => {
            if (txt.includes(kw.toLowerCase())) hitCount++;
          });
          const isCorrect = hitCount >= 2 || txt.length >= 30;
          handleAnswerResult(q, isCorrect, area.value.trim());
          modelBox.style.display = 'block';
        };
      }
    }

    function handleAnswerResult(q, isCorrect, selectedVal) {
      if (!userAnswers[q.id]) {
        userAnswers[q.id] = { answered: true, isCorrect: isCorrect, selected: selectedVal };
        if (isCorrect) {
          score += 2;
          playCorrectSound();
          triggerConfetti();
        } else {
          playWrongSound();
          triggerScreenShake();
        }
      }
      loadQuestion();
    }

    function navigateQuestion(step) {
      const newIdx = currentIndex + step;
      if (newIdx < 0) return;
      if (newIdx >= filteredQuestions.length) {
        showQuizFinalResult();
        return;
      }
      currentIndex = newIdx;
      loadQuestion();
    }

    function triggerConfetti() {
      if (typeof confetti === 'function') {
        confetti({
          particleCount: 65,
          spread: 70,
          origin: { y: 0.7 }
        });
      }
    }

    function triggerScreenShake() {
      const box = document.getElementById('questionContainer') || document.getElementById('viewLogin');
      if (box) {
        box.classList.remove('shake-anim');
        void box.offsetWidth;
        box.classList.add('shake-anim');
      }
    }

    // =========================================================================
    // 6. RESULTS, CERTIFICATE & STORAGE
    // =========================================================================
    function showQuizFinalResult() {
      switchView('result');
      
      const totalAnswers = Object.keys(userAnswers).length;
      let correctAnswers = 0;
      Object.values(userAnswers).forEach(ans => {
        if (ans.isCorrect) correctAnswers++;
      });

      const finalScore = Math.round((correctAnswers / QUIZ_DATA.length) * 100);

      document.getElementById('resStudentName').textContent = currentUser.name || 'Học sinh';
      document.getElementById('resStudentClass').textContent = currentUser.className || '7';
      document.getElementById('resFinalScore').textContent = `${finalScore}/100`;

      document.getElementById('statCorrectCount').textContent = correctAnswers;
      document.getElementById('statAccuracy').textContent = `${Math.round((correctAnswers / (totalAnswers || 1)) * 100)}%`;
      document.getElementById('statCompleted').textContent = `${totalAnswers}/50`;

      const evalEl = document.getElementById('resEvaluation');
      if (finalScore >= 80) {
        evalEl.textContent = '🌟 Xuất sắc! Em đã nắm rất vững kiến thức Bài 4 - Bảng tuần hoàn!';
        evalEl.style.color = '#34d399';
        triggerConfetti();
      } else if (finalScore >= 60) {
        evalEl.textContent = '👍 Khá tốt! Em hãy ôn lại một số câu sai để đạt điểm tối đa nhé!';
        evalEl.style.color = '#38bdf8';
      } else {
        evalEl.textContent = '💪 Cần cố gắng hơn! Hãy xem lại phần Lý Thuyết & Video để nắm vững bài hơn.';
        evalEl.style.color = '#fbbf24';
      }

      saveToLeaderboard(currentUser.name || 'Học sinh ẩn danh', currentUser.className || '7', finalScore);
    }

    function saveToLeaderboard(name, cls, userScore) {
      let board = JSON.parse(safeStorage.getItem('khtn7_leaderboard') || '[]');
      board.push({
        name: name,
        cls: cls,
        score: userScore,
        date: new Date().toLocaleDateString('vi-VN')
      });
      board.sort((a, b) => b.score - a.score);
      board = board.slice(0, 5);
      safeStorage.setItem('khtn7_leaderboard', JSON.stringify(board));
    }

    function renderLeaderboard() {
      const container = document.getElementById('leaderboardList');
      if (!container) return;
      const board = JSON.parse(safeStorage.getItem('khtn7_leaderboard') || '[]');

      if (board.length === 0) {
        container.innerHTML = `
          <div style="text-align:center; padding:2rem; color:var(--text-muted);">
            <i class="fa-solid fa-folder-open" style="font-size:2rem; margin-bottom:0.5rem;"></i>
            <p>Chưa có bạn nào hoàn thành bài thi. Hãy là người đầu tiên ghi danh!</p>
          </div>
        `;
        return;
      }

      container.innerHTML = '';
      board.forEach((item, index) => {
        const row = document.createElement('div');
        row.className = 'leader-row';
        const rankClass = index === 0 ? 'rank-1' : (index === 1 ? 'rank-2' : (index === 2 ? 'rank-3' : ''));
        row.innerHTML = `
          <div style="display:flex; align-items:center; gap:12px;">
            <span class="leader-rank ${rankClass}">#${index + 1}</span>
            <div>
              <div style="font-weight:700; color:#fff;">${item.name}</div>
              <div style="font-size:0.75rem; color:var(--text-muted);">Lớp ${item.cls} • ${item.date}</div>
            </div>
          </div>
          <div style="font-weight:800; font-size:1.1rem; color:var(--accent-cyan);">
            ${item.score} <span style="font-size:0.75rem; color:var(--text-muted);">điểm</span>
          </div>
        `;
        container.appendChild(row);
      });
    }

    function clearLeaderboardData() {
      if (confirm('Em có chắc chắn muốn xóa lịch sử bảng xếp hạng trên thiết bị này?')) {
        safeStorage.removeItem('khtn7_leaderboard');
        renderLeaderboard();
      }
    }

    function restartQuiz() {
      userAnswers = {};
      score = 0;
      currentIndex = 0;
      switchView('quiz');
      loadQuestion();
    }

    function exportResultImage() {
      const card = document.getElementById('reportCardArea');
      if (!window.html2canvas) {
        alert('Đang tải thư viện ảnh, vui lòng thử lại sau giây lát!');
        return;
      }

      html2canvas(card, {
        backgroundColor: '#0f172a',
        scale: 2
      }).then(canvas => {
        const link = document.createElement('a');
        link.download = `Bao-Cao-Ket-Qua-KHTN7-${currentUser.name || 'HocSinh'}.png`;
        link.href = canvas.toDataURL('image/png');
        link.click();
      }).catch(err => {
        console.error('Export error:', err);
        alert('Có lỗi khi tạo ảnh báo cáo kết quả.');
      });
    }
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_head)
    f.write(quiz_code)
    f.write("\n")
    f.write(html_tail)

print("Regenerated fixed index.html successfully!")
