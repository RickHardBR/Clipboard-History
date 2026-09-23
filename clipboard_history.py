import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import ttkbootstrap as tb
from collections import deque
from PIL import ImageGrab, Image, ImageTk
import os
import hashlib
import time
import json
import sys

# --- Configurations ---
MAX_ITEMS = 10
MAX_DELETED = 50
IMAGE_DIR = "clipboard_images"
CONFIG_FILE = "config.json"

if not os.path.exists(IMAGE_DIR):
  os.makedirs(IMAGE_DIR)

DEFAULT_CONFIG = {"theme": "dark", "accent_color": "#7c5cff", "language": "pt_BR"}

TRANSLATIONS = {
  "pt_BR": {
    "app_title": "Clipboard History Manager",
    "monitoring": "monitorando...",
    "menu_file": "Arquivo",
    "menu_save_txt": "Salvar TXT",
    "menu_exit": "Sair",
    "menu_edit": "Editar",
    "menu_delete": "Excluir",
    "menu_deleted": "Apagados (Lixeira)",
    "menu_view": "Exibir",
    "menu_settings": "Configuracoes",
    "menu_preferences": "Preferencias",
    "tab_texts": "Textos",
    "tab_links": "Links",
    "tab_images": "Imagens",
    "view_label": "Visualizacao:",
    "view_details": "Detalhes",
    "view_small": "Icones Pequenos",
    "view_medium": "Icones Medios",
    "view_large": "Icones Grandes",
    "no_items": "Nenhum item capturado ainda.",
    "btn_copy": "Copiar Selecionado",
    "btn_delete": "Excluir",
    "btn_save_txt": "Salvar TXT",
    "btn_save_img": "Salvar Imagem",
    "btn_deleted": "Apagados",
    "dialog_warn_title": "Aviso",
    "dialog_warn_select": "Selecione um item primeiro.",
    "dialog_copied_title": "Copiado",
    "dialog_copied_msg": "Item copiado para a area de transferencia!",
    "dialog_copy_img_warn": "Copiar imagens requer win32clipboard.",
    "dialog_confirm_del_title": "Confirmar Exclusao",
    "dialog_confirm_del_msg": "Mover para os apagados?",
    "dialog_confirm_del_img_msg": "Mover imagem para os apagados?",
    "dialog_txt_only_msg": "Esta funcao suporta apenas textos e links.",
    "dialog_success_title": "Sucesso",
    "dialog_file_saved_msg": "Arquivo salvo!",
    "dialog_error_title": "Erro",
    "dialog_error_msg": "Erro:\n{}",
    "edit_window_title": "Visualizar / Editar",
    "edit_window_header": "Editar Texto",
    "edit_window_save": "Salvar Correcao",
    "image_window_title": "Visualizar Imagem",
    "image_load_error": "Erro ao carregar:\n{}",
    "deleted_window_title": "Lixeira",
    "deleted_window_header": "Lixeira",
    "deleted_tag_image": "[IMAGEM]",
    "deleted_confirm_perm_title": "Excluir Definitivamente",
    "deleted_confirm_perm_msg": "Excluir para sempre?",
    "deleted_btn_restore": "Restaurar",
    "deleted_btn_delete_perm": "Excluir Definitivo",
    "pref_title": "Preferencias",
    "pref_theme": "Tema Visual",
    "pref_theme_dark": "Escuro",
    "pref_theme_light": "Claro",
    "pref_accent": "Cor de Destaque",
    "pref_color_purple": "Roxo",
    "pref_color_teal": "Verde-agua",
    "pref_color_blue": "Azul",
    "pref_color_red": "Vermelho",
    "pref_language": "Idioma",
    "pref_lang_pt": "Portugues (Brasil)",
    "pref_lang_en": "English",
    "pref_lang_es": "Espanol",
    "pref_btn_save": "Aplicar e Salvar",
    "pref_saved_title": "Preferencias",
    "pref_saved_msg": "Configuracoes aplicadas e salvas com sucesso!",
  },
  "en_US": {
    "app_title": "Clipboard History Manager",
    "monitoring": "monitoring...",
    "menu_file": "File",
    "menu_save_txt": "Save TXT",
    "menu_exit": "Exit",
    "menu_edit": "Edit",
    "menu_delete": "Delete",
    "menu_deleted": "Trash (Recycle Bin)",
    "menu_view": "View",
    "menu_settings": "Settings",
    "menu_preferences": "Preferences",
    "tab_texts": "Texts",
    "tab_links": "Links",
    "tab_images": "Images",
    "view_label": "View Mode:",
    "view_details": "Details",
    "view_small": "Small Icons",
    "view_medium": "Medium Icons",
    "view_large": "Large Icons",
    "no_items": "No items captured yet.",
    "btn_copy": "Copy Selected",
    "btn_delete": "Delete",
    "btn_save_txt": "Save TXT",
    "btn_save_img": "Save Image",
    "btn_deleted": "Trash",
    "dialog_warn_title": "Warning",
    "dialog_warn_select": "Please select an item first.",
    "dialog_copied_title": "Copied",
    "dialog_copied_msg": "Item copied to clipboard!",
    "dialog_copy_img_warn": "Copying images requires win32clipboard.",
    "dialog_confirm_del_title": "Confirm Deletion",
    "dialog_confirm_del_msg": "Move item to trash?",
    "dialog_confirm_del_img_msg": "Move image to trash?",
    "dialog_txt_only_msg": "This function only supports text and links.",
    "dialog_success_title": "Success",
    "dialog_file_saved_msg": "File saved successfully!",
    "dialog_error_title": "Error",
    "dialog_error_msg": "Error:\n{}",
    "edit_window_title": "View / Edit",
    "edit_window_header": "Edit Text",
    "edit_window_save": "Save Changes",
    "image_window_title": "View Image",
    "image_load_error": "Error loading:\n{}",
    "deleted_window_title": "Recycle Bin",
    "deleted_window_header": "Recycle Bin",
    "deleted_tag_image": "[IMAGE]",
    "deleted_confirm_perm_title": "Permanently Delete",
    "deleted_confirm_perm_msg": "Delete permanently?",
    "deleted_btn_restore": "Restore",
    "deleted_btn_delete_perm": "Permanently Delete",
    "pref_title": "Preferences",
    "pref_theme": "Visual Theme",
    "pref_theme_dark": "Dark",
    "pref_theme_light": "Light",
    "pref_accent": "Accent Color",
    "pref_color_purple": "Purple",
    "pref_color_teal": "Teal",
    "pref_color_blue": "Blue",
    "pref_color_red": "Red",
    "pref_language": "Language",
    "pref_lang_pt": "Portugues (Brasil)",
    "pref_lang_en": "English",
    "pref_lang_es": "Espanol",
    "pref_btn_save": "Apply & Save",
    "pref_saved_title": "Preferences",
    "pref_saved_msg": "Settings applied and saved successfully!",
  },
  "es_ES": {
    "app_title": "Clipboard History Manager",
    "monitoring": "monitoreando...",
    "menu_file": "Archivo",
    "menu_save_txt": "Guardar TXT",
    "menu_exit": "Salir",
    "menu_edit": "Editar",
    "menu_delete": "Eliminar",
    "menu_deleted": "Papelera",
    "menu_view": "Ver",
    "menu_settings": "Configuracion",
    "menu_preferences": "Preferencias",
    "tab_texts": "Textos",
    "tab_links": "Enlaces",
    "tab_images": "Imagenes",
    "view_label": "Vista:",
    "view_details": "Detalles",
    "view_small": "Iconos Pequenos",
    "view_medium": "Iconos Medianos",
    "view_large": "Iconos Grandes",
    "no_items": "Ningun elemento capturado aun.",
    "btn_copy": "Copiar Seleccion",
    "btn_delete": "Eliminar",
    "btn_save_txt": "Guardar TXT",
    "btn_save_img": "Guardar Imagen",
    "btn_deleted": "Papelera",
    "dialog_warn_title": "Aviso",
    "dialog_warn_select": "Seleccione un elemento primero.",
    "dialog_copied_title": "Copiado",
    "dialog_copied_msg": "Elemento copiado al portapapeles!",
    "dialog_copy_img_warn": "Copiar imagenes requiere win32clipboard.",
    "dialog_confirm_del_title": "Confirmar Eliminacion",
    "dialog_confirm_del_msg": "Mover a la papelera?",
    "dialog_confirm_del_img_msg": "Mover imagen a la papelera?",
    "dialog_txt_only_msg": "Esta funcion solo admite textos e enlaces.",
    "dialog_success_title": "Exito",
    "dialog_file_saved_msg": "Archivo guardado con exito!",
    "dialog_error_title": "Error",
    "dialog_error_msg": "Error:\n{}",
    "edit_window_title": "Ver / Editar",
    "edit_window_header": "Editar Texto",
    "edit_window_save": "Guardar Cambios",
    "image_window_title": "Ver Imagen",
    "image_load_error": "Error al cargar:\n{}",
    "deleted_window_title": "Papelera",
    "deleted_window_header": "Papelera",
    "deleted_tag_image": "[IMAGEN]",
    "deleted_confirm_perm_title": "Eliminar Definitivamente",
    "deleted_confirm_perm_msg": "Eliminar para siempre?",
    "deleted_btn_restore": "Restaurar",
    "deleted_btn_delete_perm": "Eliminar Definitivo",
    "pref_title": "Preferencias",
    "pref_theme": "Tema Visual",
    "pref_theme_dark": "Oscuro",
    "pref_theme_light": "Claro",
    "pref_accent": "Color de Enfasis",
    "pref_color_purple": "Purpura",
    "pref_color_teal": "Verde azulado",
    "pref_color_blue": "Azul",
    "pref_color_red": "Rojo",
    "pref_language": "Idioma",
    "pref_lang_pt": "Portugues (Brasil)",
    "pref_lang_en": "English",
    "pref_lang_es": "Espanol",
    "pref_btn_save": "Aplicar y Guardar",
    "pref_saved_title": "Preferencias",
    "pref_saved_msg": "Configuracion aplicada y guardada con exito!",
  }
}

def load_config():
  if os.path.exists(CONFIG_FILE):
    try:
      with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        DEFAULT_CONFIG.update(json.load(f))
    except: pass

def save_config(theme, accent, language="pt_BR"):
  DEFAULT_CONFIG['theme'] = theme
  DEFAULT_CONFIG['accent_color'] = accent
  DEFAULT_CONFIG['language'] = language
  try:
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
      json.dump(DEFAULT_CONFIG, f, indent=4)
  except: pass

load_config()

def t(key, *args):
  lang = DEFAULT_CONFIG.get("language", "pt_BR")
  text = TRANSLATIONS.get(lang, TRANSLATIONS["pt_BR"]).get(key, TRANSLATIONS["pt_BR"].get(key, key))
  if args:
    try:
      return text.format(*args)
    except Exception:
      return text
  return text

def get_palette():
  is_dark = DEFAULT_CONFIG['theme'] == "dark"
  a = DEFAULT_CONFIG['accent_color']
  return {
    "bg":      "#17172a" if is_dark else "#f8f9fa",
    "sec_bg":  "#20203a" if is_dark else "#e9ecef",
    "ter_bg":  "#2a2a48" if is_dark else "#dee2e6",
    "border":  "#35355a" if is_dark else "#ced4da",
    "fg":      "#e0e0e0" if is_dark else "#212529",
    "fg_dim":  "#6a6a8a" if is_dark else "#6c757d",
    "accent":  a,
    "danger":  "#e05263",
    "success": "#2aae82",
    "is_dark": is_dark,
  }

# --- Data Structures ---
history = {k: deque(maxlen=MAX_ITEMS)  for k in ('text', 'link', 'image')}
deleted_history = {k: deque(maxlen=MAX_DELETED) for k in ('text', 'link', 'image')}

# --- UI Globals ---
edit_window        = None
deleted_window     = None
settings_window    = None
image_view_mode    = "Detalhes"
image_buttons      = []
selected_image_index = None
current_tab_index  = 0
TAB_CATS           = ['text', 'link', 'image']
custom_list_text   = None
custom_list_link   = None

# ============================================================
# ROUNDED BUTTON
# ============================================================
class RoundedButton(tk.Canvas):
  def __init__(self, parent, text, command=None,
               bg="#7c5cff", fg="#ffffff",
               hover_bg=None, active_bg=None,
               radius=16, width=150, height=40,
               font=("Arial", 10, "bold"),
               border_color=None, border_width=0, **kwargs):
    try:
      _cbg = parent.cget('bg')
    except Exception:
      _cbg = '#17172a'
    super().__init__(parent, width=width, height=height,
                     highlightthickness=0, bd=0, takefocus=0, bg=_cbg, **kwargs)
    self.command    = command
    self.bg_normal  = bg
    self.bg_hover   = hover_bg  or self._shift(bg, +22)
    self.bg_active  = active_bg or self._shift(bg, -22)
    self.fg         = fg
    self.radius     = radius
    self.btn_text   = text
    self.btn_font   = font
    self.border_color  = border_color
    self.border_width  = border_width
    self.bind("<Enter>",           lambda e: self._draw(self.bg_hover))
    self.bind("<Leave>",           lambda e: self._draw(self.bg_normal))
    self.bind("<ButtonPress-1>",   lambda e: self._draw(self.bg_active))
    self.bind("<ButtonRelease-1>", lambda e: self._release())
    self._draw(self.bg_normal)

  def _shift(self, h, amt):
    h = h.lstrip('#')
    r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    clamp = lambda v: max(0, min(255, v + amt))
    return "#{:02x}{:02x}{:02x}".format(clamp(r), clamp(g), clamp(b))

  def _draw(self, fill):
    self.delete("all")
    w, h, r = int(self["width"]), int(self["height"]), self.radius
    pts = [r,0, w-r,0, w,0, w,r, w,h-r, w,h,
           w-r,h, r,h, 0,h, 0,h-r, 0,r, 0,0, r,0]
    self.create_polygon(pts, smooth=True, fill=fill, outline=fill)
    if self.border_color and self.border_width:
      self.create_polygon(pts, smooth=True, fill="",
                          outline=self.border_color, width=self.border_width)
    self.create_text(w//2, h//2, text=self.btn_text, fill=self.fg,
                      font=self.btn_font, anchor="center")

  def _release(self):
    self._draw(self.bg_hover)
    if self.command: self.command()

  def set_text(self, text):
    self.btn_text = text
    self._draw(self.bg_normal)

  def set_colors(self, bg=None, fg=None, hover_bg=None, active_bg=None,
                 border_color=None, border_width=None, parent_bg=None):
    if bg is not None:
      self.bg_normal = bg
      self.bg_hover = hover_bg or self._shift(bg, +22)
      self.bg_active = active_bg or self._shift(bg, -22)
    if fg is not None: self.fg = fg
    if border_color is not None: self.border_color = border_color
    if border_width is not None: self.border_width = border_width
    if parent_bg is not None:
      self.config(bg=parent_bg)
    self._draw(self.bg_normal)

# ============================================================
# CUSTOM TAB BAR — underline indicator style
# ============================================================
class CustomTabBar(tk.Frame):
  def __init__(self, parent, tabs, on_change, palette, **kwargs):
    p = palette
    super().__init__(parent, bg=p["bg"], **kwargs)
    self.palette   = p
    self.on_change = on_change
    self._widgets  = []
    self.active    = 0

    for i, (icon, label) in enumerate(tabs):
      col = tk.Frame(self, bg=p["bg"], cursor="hand2")
      col.pack(side="left", padx=(0, 6))

      row = tk.Frame(col, bg=p["bg"])
      row.pack()

      il = tk.Label(row, text=icon, font=("Arial", 10),
                    bg=p["bg"], fg=p["fg_dim"], cursor="hand2")
      il.pack(side="left")

      tl = tk.Label(row, text=f" {label}", font=("Arial", 11),
                    bg=p["bg"], fg=p["fg_dim"],
                    padx=4, pady=10, cursor="hand2")
      tl.pack(side="left")

      ind = tk.Frame(col, bg=p["bg"], height=2)
      ind.pack(fill="x")

      self._widgets.append((col, row, il, tl, ind))
      for w in (col, row, il, tl):
        w.bind("<Button-1>", lambda e, idx=i: self.switch_to(idx))

    self.switch_to(0)

  def switch_to(self, idx):
    p = self.palette
    for i, (col, row, il, tl, ind) in enumerate(self._widgets):
      if i == idx:
        il.config(fg=p["accent"])
        tl.config(fg=p["accent"], font=("Arial", 11, "bold"))
        ind.config(bg=p["accent"])
      else:
        il.config(fg=p["fg_dim"])
        tl.config(fg=p["fg_dim"], font=("Arial", 11))
        ind.config(bg=p["bg"])
    self.active = idx
    self.on_change(idx)

  def update_palette_and_labels(self, palette, tabs=None):
    p = palette
    self.palette = p
    self.config(bg=p["bg"])
    for i, (col, row, il, tl, ind) in enumerate(self._widgets):
      col.config(bg=p["bg"])
      row.config(bg=p["bg"])
      if tabs and i < len(tabs):
        icon, label = tabs[i]
        il.config(text=icon)
        tl.config(text=f" {label}")
      if i == self.active:
        il.config(bg=p["bg"], fg=p["accent"])
        tl.config(bg=p["bg"], fg=p["accent"], font=("Arial", 11, "bold"))
        ind.config(bg=p["accent"])
      else:
        il.config(bg=p["bg"], fg=p["fg_dim"])
        tl.config(bg=p["bg"], fg=p["fg_dim"], font=("Arial", 11))
        ind.config(bg=p["bg"])

# ============================================================
# CUSTOM SCROLLABLE LIST — itens com pill arredondado
# ============================================================
class CustomList(tk.Frame):
  def __init__(self, parent, palette, on_select=None, **kwargs):
    p = palette
    super().__init__(parent, bg=p["sec_bg"], **kwargs)
    self.palette      = p
    self.on_select    = on_select
    self.items        = []
    self.selected_index = None

    self._cv   = tk.Canvas(self, bg=p["sec_bg"], bd=0, highlightthickness=0)
    self._sb   = ttk.Scrollbar(self, orient="vertical", command=self._cv.yview)
    self._inner = tk.Frame(self._cv, bg=p["sec_bg"])

    self._inner.bind("<Configure>",
      lambda e: self._cv.configure(scrollregion=self._cv.bbox("all")))
    self._cwin = self._cv.create_window((0, 0), window=self._inner, anchor="nw")
    self._cv.configure(yscrollcommand=self._sb.set)
    self._cv.bind("<Configure>",
      lambda e: self._cv.itemconfig(self._cwin, width=e.width))

    self._cv.pack(side="left", expand=True, fill="both")
    self._sb.pack(side="right", fill="y")

    for w in (self._cv, self._inner):
      w.bind("<MouseWheel>",
        lambda e: self._cv.yview_scroll(int(-1*(e.delta/120)), "units"))

  def update_palette(self, palette):
    self.palette = palette
    self.config(bg=palette["sec_bg"])
    self._cv.config(bg=palette["sec_bg"])
    self._inner.config(bg=palette["sec_bg"])
    self._rebuild()

  def populate(self, full_items):
    self.items          = list(full_items)
    self.selected_index = None
    self._rebuild()

  def _rebuild(self):
    p = self.palette
    for w in self._inner.winfo_children():
      w.destroy()

    if not self.items:
      tk.Label(self._inner, text=t("no_items"),
               font=("Arial", 11), bg=p["sec_bg"],
               fg=p["fg_dim"], pady=24).pack()
      return

    for i, full_text in enumerate(self.items):
      preview = full_text.replace("\n", " ")[:95]
      is_sel  = (i == self.selected_index)
      self._make_row(i, preview, is_sel)

      # Separator (somente entre itens não selecionados)
      if i < len(self.items) - 1 and not is_sel and i + 1 != self.selected_index:
        sep = tk.Frame(self._inner, bg=p["border"], height=1)
        sep.pack(fill="x", padx=20)

  def _make_row(self, idx, preview, is_sel):
    p = self.palette

    outer = tk.Frame(self._inner, bg=p["sec_bg"])
    outer.pack(fill="x", padx=10, pady=(5 if idx == 0 else 3, 3))

    if is_sel:
      # Canvas com rounded rectangle
      rc = tk.Canvas(outer, bg=p["sec_bg"], bd=0,
                     highlightthickness=0, height=46)
      rc.pack(fill="x")

      def draw_pill(ev=None, c=rc, txt=preview):
        c.delete("all")
        cw = c.winfo_width() or 500
        ch = int(c["height"])
        r  = 12
        x1, y1, x2, y2 = 0, 2, cw, ch - 2
        pts = [x1+r,y1, x2-r,y1, x2,y1, x2,y1+r,
               x2,y2-r, x2,y2, x2-r,y2, x1+r,y2,
               x1,y2, x1,y2-r, x1,y1+r, x1,y1, x1+r,y1]
        c.create_polygon(pts, smooth=True, fill=p["accent"], outline=p["accent"])
        c.create_text(20, ch//2, text=txt, fill="#ffffff",
                      font=("Arial", 11, "bold"), anchor="w")

      rc.bind("<Configure>", draw_pill)
      rc.bind("<Button-1>",  lambda e, i=idx: self._on_click(i))
      rc.after(10, draw_pill)
    else:
      row = tk.Frame(outer, bg=p["sec_bg"], cursor="hand2")
      row.pack(fill="x")

      lbl = tk.Label(row, text=preview, font=("Arial", 11),
                     bg=p["sec_bg"], fg=p["fg"],
                     anchor="w", padx=16, pady=11)
      lbl.pack(fill="x")

      def enter(e, rw=row, lb=lbl):
        rw.config(bg=p["ter_bg"]); lb.config(bg=p["ter_bg"])
      def leave(e, rw=row, lb=lbl):
        rw.config(bg=p["sec_bg"]); lb.config(bg=p["sec_bg"])

      for w in (row, lbl):
        w.bind("<Button-1>", lambda e, i=idx: self._on_click(i))
        w.bind("<Enter>", enter)
        w.bind("<Leave>", leave)

  def _on_click(self, idx):
    self.selected_index = idx
    self._rebuild()
    if self.on_select:
      self.on_select(idx, self.items[idx])

  def get_selected(self):
    if self.selected_index is not None and self.selected_index < len(self.items):
      return self.selected_index, self.items[self.selected_index]
    return None, None

  def clear_selection(self):
    self.selected_index = None
    self._rebuild()

# ============================================================
# CLIPBOARD LOGIC
# ============================================================
def get_image_hash(img):
  return hashlib.md5(img.tobytes()).hexdigest()

def is_clipboard_matching(cat, item):
  try:
    if cat == 'image':
      cur_img = ImageGrab.grabclipboard()
      if isinstance(cur_img, Image.Image):
        target_hash = item.get('hash') if isinstance(item, dict) else item
        return get_image_hash(cur_img) == target_hash
      return False
    else:
      cur_text = root.clipboard_get()
      cur_norm = cur_text.strip().replace('\r\n', '\n')
      item_norm = item.strip().replace('\r\n', '\n')
      return cur_norm == item_norm
  except Exception:
    return False

def clear_clipboard_if_matches(cat, item):
  try:
    if is_clipboard_matching(cat, item):
      root.clipboard_clear()
  except Exception:
    pass

def handle_image(img):
  img_hash = get_image_hash(img)
  filepath = os.path.join(IMAGE_DIR, f"{img_hash}.png")
  for item in history['image']:
    if item['hash'] == img_hash: return
  for item in deleted_history['image']:
    if item['hash'] == img_hash: return
  img.save(filepath, format="PNG")
  history['image'].appendleft({'hash': img_hash, 'path': filepath,
                                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")})
  if current_tab_index == 2:
    update_images_view()

def handle_text(text):
  if not text: return
  is_link = text.startswith("http://") or text.startswith("https://")
  cat = 'link' if is_link else 'text'
  if text in history[cat] or text in deleted_history[cat]: return
  history[cat].appendleft(text)
  if (current_tab_index == 0 and cat == 'text') or \
     (current_tab_index == 1 and cat == 'link'):
    update_list_view(cat)

def save_clipboard():
  try:
    img = ImageGrab.grabclipboard()
    if isinstance(img, Image.Image):
      handle_image(img)
    else:
      try:
        text = root.clipboard_get().strip()
        handle_text(text)
      except tk.TclError: pass
  except Exception: pass
  root.after(1000, save_clipboard)

# ============================================================
# UI UPDATES
# ============================================================
def get_current_category():
  return TAB_CATS[current_tab_index]

def update_list_view(cat=None):
  if cat is None: cat = get_current_category()
  if cat == 'image':
    update_images_view()
    return
  cl = custom_list_text if cat == 'text' else custom_list_link
  if cl: cl.populate(list(history[cat]))

def update_images_view():
  for w in images_inner_frame.winfo_children():
    w.destroy()
  global image_buttons
  image_buttons.clear()
  p = get_palette()

  if image_view_mode == "Detalhes":
    for i, item in enumerate(history['image']):
      lbl = tk.Label(images_inner_frame,
                     text=f"  {item['timestamp']}  —  {item['hash'][:8]}.png",
                     font=("Arial", 11), anchor="w", bg=p["sec_bg"],
                     fg=p["fg"], padx=12, pady=8, cursor="hand2")
      lbl.pack(fill="x", padx=10, pady=3)
      lbl.bind("<Button-1>", lambda e, idx=i: select_image(idx))
      lbl.bind("<Enter>",    lambda e, l=lbl: l.config(bg=p["ter_bg"]))
      lbl.bind("<Leave>",    lambda e, l=lbl: l.config(bg=p["sec_bg"]))
      image_buttons.append(lbl)
  else:
    size_map = {"Icones Pequenos": 64, "Icones Medios": 128, "Icones Grandes": 256}
    size = size_map.get(image_view_mode, 128)
    col, row = 0, 0
    max_cols = max(1, images_canvas.winfo_width() // (size + 30))
    for i, item in enumerate(history['image']):
      try:
        img = Image.open(item['path'])
        img.thumbnail((size, size))
        photo = ImageTk.PhotoImage(img)
        btn = tk.Label(images_inner_frame, image=photo,
                       bg=p["sec_bg"], cursor="hand2", relief="flat", bd=0)
        btn.image = photo
        btn.bind("<Button-1>", lambda e, idx=i: select_image(idx))
        btn.grid(row=row, column=col, padx=10, pady=10)
        image_buttons.append(btn)
        col += 1
        if col >= max_cols: col, row = 0, row + 1
      except Exception: pass

  images_inner_frame.update_idletasks()
  images_canvas.config(scrollregion=images_canvas.bbox("all"))

def on_tab_change(idx):
  global current_tab_index, selected_image_index
  current_tab_index = idx
  selected_image_index = None
  cat = TAB_CATS[idx]

  # tab_frames may not exist yet during initial CustomTabBar construction
  if 'tab_frames' in globals():
    for i, frame in enumerate(tab_frames):
      if i == idx:
        frame.pack(expand=True, fill="both")
      else:
        frame.pack_forget()

  update_list_view(cat)

  if 'frame_image_controls' in globals():
    if cat == 'image':
      frame_image_controls.pack(fill="x", padx=20, pady=(0, 6))
    else:
      frame_image_controls.pack_forget()

  if 'btn_save' in globals() and btn_save:
    btn_save.set_text(t("btn_save_img") if cat == 'image' else t("btn_save_txt"))

def change_view_mode(mode):
  global image_view_mode, selected_image_index
  image_view_mode = mode
  selected_image_index = None
  update_images_view()

# ============================================================
# INTERACTIONS
# ============================================================
def select_image(index):
  global selected_image_index
  selected_image_index = index
  p = get_palette()
  for i, btn in enumerate(image_buttons):
    sel = (i == index)
    if image_view_mode == "Detalhes":
      btn.config(bg=p["accent"] if sel else p["sec_bg"],
                 fg="#ffffff" if sel else p["fg"])
    else:
      btn.config(bg=p["accent"] if sel else p["sec_bg"])
  open_image_window(index)

def copy_selected():
  cat = get_current_category()
  if cat in ('text', 'link'):
    cl = custom_list_text if cat == 'text' else custom_list_link
    idx, text = cl.get_selected()
    if idx is None:
      messagebox.showwarning(t("dialog_warn_title"), t("dialog_warn_select"))
      return
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo(t("dialog_copied_title"), t("dialog_copied_msg"))
  elif cat == 'image':
    messagebox.showwarning(t("dialog_warn_title"), t("dialog_copy_img_warn"))

def delete_selected():
  global selected_image_index, edit_window
  cat = get_current_category()
  if cat in ('text', 'link'):
    cl = custom_list_text if cat == 'text' else custom_list_link
    idx, text = cl.get_selected()
    if idx is None:
      messagebox.showwarning(t("dialog_warn_title"), t("dialog_warn_select"))
      return
    if messagebox.askyesno(t("dialog_confirm_del_title"), t("dialog_confirm_del_msg")):
      tmp = list(history[cat])
      deleted = tmp.pop(idx)
      history[cat].clear()
      for x in tmp: history[cat].append(x)
      deleted_history[cat].appendleft(deleted)
      clear_clipboard_if_matches(cat, deleted)
      update_list_view(cat)
      if edit_window and edit_window.winfo_exists(): edit_window.destroy()
  elif cat == 'image':
    if selected_image_index is None or selected_image_index >= len(history['image']):
      messagebox.showwarning(t("dialog_warn_title"), t("dialog_warn_select"))
      return
    if messagebox.askyesno(t("dialog_confirm_del_title"), t("dialog_confirm_del_img_msg")):
      tmp = list(history['image'])
      deleted = tmp.pop(selected_image_index)
      history['image'].clear()
      for x in tmp: history['image'].append(x)
      deleted_history['image'].appendleft(deleted)
      clear_clipboard_if_matches('image', deleted)
      selected_image_index = None
      update_list_view('image')
      if edit_window and edit_window.winfo_exists(): edit_window.destroy()

def save_as_file():
  cat = get_current_category()
  if cat == 'image':
    if selected_image_index is None or selected_image_index >= len(history['image']):
      messagebox.showwarning(t("dialog_warn_title"), t("dialog_warn_select"))
      return
    item = list(history['image'])[selected_image_index]
    filepath = filedialog.asksaveasfilename(
      defaultextension=".png",
      filetypes=[
        ("PNG Image", "*.png"),
        ("JPEG Image", "*.jpg;*.jpeg"),
        ("Bitmap Image", "*.bmp"),
        ("All Files", "*.*")
      ]
    )
    if filepath:
      try:
        img = Image.open(item['path'])
        ext = os.path.splitext(filepath)[1].lower()
        if ext in ('.jpg', '.jpeg') and img.mode in ('RGBA', 'LA', 'P'):
          img = img.convert('RGB')
        img.save(filepath)
        messagebox.showinfo(t("dialog_success_title"), t("dialog_file_saved_msg"))
      except Exception as e:
        messagebox.showerror(t("dialog_error_title"), t("dialog_error_msg", e))
  else:
    cl = custom_list_text if cat == 'text' else custom_list_link
    idx, text = cl.get_selected()
    if idx is None:
      messagebox.showwarning(t("dialog_warn_title"), t("dialog_warn_select"))
      return
    filepath = filedialog.asksaveasfilename(
      defaultextension=".txt",
      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filepath:
      try:
        with open(filepath, 'w', encoding='utf-8') as f:
          f.write(text)
        messagebox.showinfo(t("dialog_success_title"), t("dialog_file_saved_msg"))
      except Exception as e:
        messagebox.showerror(t("dialog_error_title"), t("dialog_error_msg", e))

save_as_txt = save_as_file

def open_edit_window(idx, text, cat):
  global edit_window
  if edit_window and edit_window.winfo_exists(): edit_window.destroy()
  p = get_palette()

  edit_window = tb.Toplevel(root)
  edit_window.title(t("edit_window_title"))
  edit_window.geometry(f"520x400+{root.winfo_x()+root.winfo_width()+20}+{root.winfo_y()}")
  edit_window.configure(bg=p["bg"])

  tk.Label(edit_window, text=t("edit_window_header"), font=("Arial", 14, "bold"),
           bg=p["bg"], fg=p["fg"]).pack(pady=(18, 4), padx=20, anchor="w")
  tk.Frame(edit_window, bg=p["border"], height=1).pack(fill="x", padx=20, pady=(0, 12))

  tw = tk.Text(edit_window, wrap="word", font=("Arial", 12),
               bg=p["sec_bg"], fg=p["fg"],
               insertbackground=p["fg"],
               selectbackground=p["accent"], selectforeground="#fff",
               padx=12, pady=10, bd=0, relief="flat",
               highlightthickness=1,
               highlightbackground=p["border"], highlightcolor=p["accent"])
  tw.pack(expand=True, fill="both", padx=20, pady=(0, 12))
  tw.insert("1.0", text)

  def save_edit():
    new = tw.get("1.0", "end-1c").strip()
    tmp = list(history[cat])
    tmp[idx] = new
    history[cat].clear()
    for x in tmp: history[cat].append(x)
    update_list_view(cat)
    edit_window.destroy()

  RoundedButton(edit_window, text=t("edit_window_save"), command=save_edit,
                bg=p["accent"], fg="#fff", width=170, height=38
                ).pack(pady=(0, 18))

def open_image_window(index):
  global edit_window
  if edit_window and edit_window.winfo_exists(): edit_window.destroy()
  item = list(history['image'])[index]
  p = get_palette()

  edit_window = tb.Toplevel(root)
  edit_window.title(t("image_window_title"))
  edit_window.geometry(f"660x560+{root.winfo_x()+root.winfo_width()+20}+{root.winfo_y()}")
  edit_window.configure(bg=p["bg"])
  try:
    img = Image.open(item['path'])
    img.thumbnail((640, 510))
    photo = ImageTk.PhotoImage(img)
    lbl = tk.Label(edit_window, image=photo, bg=p["bg"], bd=0)
    lbl.image = photo
    lbl.pack(expand=True, fill="both", padx=10, pady=10)
    tk.Label(edit_window, text=item['timestamp'], font=("Arial", 9),
             bg=p["bg"], fg=p["fg_dim"]).pack(pady=(0, 10))
  except Exception as e:
    tk.Label(edit_window, text=t("image_load_error", e),
             bg=p["bg"], fg=p["fg"]).pack(expand=True)

def open_deleted_window():
  global deleted_window
  if deleted_window and deleted_window.winfo_exists():
    deleted_window.lift(); return
  p = get_palette()

  deleted_window = tb.Toplevel(root)
  deleted_window.title(t("deleted_window_title"))
  deleted_window.geometry(f"640x500+{root.winfo_x()+50}+{root.winfo_y()+50}")
  deleted_window.configure(bg=p["bg"])

  tk.Label(deleted_window, text=t("deleted_window_header"), font=("Arial", 15, "bold"),
           bg=p["bg"], fg=p["fg"]).pack(pady=(18,4), padx=20, anchor="w")
  tk.Frame(deleted_window, bg=p["border"], height=1).pack(fill="x", padx=20, pady=(0,10))

  cl = CustomList(deleted_window, palette=p)
  cl.pack(expand=True, fill="both", padx=20, pady=(0, 8))

  del_items_ref = []

  def refresh():
    del_items_ref.clear()
    labels = []
    for cat in ('text', 'link', 'image'):
      for item in deleted_history[cat]:
        if cat == 'image':
          labels.append(f"{t('deleted_tag_image')} {item['timestamp']}")
        else:
          labels.append(f"[{cat.upper()}] {item.replace(chr(10),' ')[:60]}")
        del_items_ref.append((cat, item))
    cl.populate(labels)

  refresh()

  def permanent_delete():
    idx, _ = cl.get_selected()
    if idx is None: return
    if messagebox.askyesno(t("deleted_confirm_perm_title"), t("deleted_confirm_perm_msg"), parent=deleted_window):
      cat, item = del_items_ref[idx]
      tmp = list(deleted_history[cat])
      tmp.remove(item)
      deleted_history[cat].clear()
      for x in tmp: deleted_history[cat].append(x)
      clear_clipboard_if_matches(cat, item)
      if cat == 'image':
        try: os.remove(item['path'])
        except: pass
      refresh()

  def restore_item():
    idx, _ = cl.get_selected()
    if idx is None: return
    cat, item = del_items_ref[idx]
    tmp = list(deleted_history[cat])
    tmp.remove(item)
    deleted_history[cat].clear()
    for x in tmp: deleted_history[cat].append(x)
    history[cat].appendleft(item)
    update_list_view(cat)
    refresh()

  bf = tk.Frame(deleted_window, bg=p["bg"])
  bf.pack(pady=14)
  RoundedButton(bf, text=t("deleted_btn_restore"), command=restore_item,
                bg=p["success"], fg="#fff", width=140, height=36).pack(side="left", padx=8)
  RoundedButton(bf, text=t("deleted_btn_delete_perm"), command=permanent_delete,
                bg=p["danger"], fg="#fff", width=164, height=36).pack(side="left", padx=8)

def open_settings():
  global settings_window
  if settings_window and settings_window.winfo_exists():
    settings_window.lift(); return
  p = get_palette()

  settings_window = tb.Toplevel(root)
  settings_window.title(t("pref_title"))
  settings_window.geometry(f"440x480+{root.winfo_x()+50}+{root.winfo_y()+50}")
  settings_window.configure(bg=p["bg"])

  tk.Label(settings_window, text=t("pref_title"), font=("Arial", 15, "bold"),
           bg=p["bg"], fg=p["fg"]).pack(pady=(18,4), padx=20, anchor="w")
  tk.Frame(settings_window, bg=p["border"], height=1).pack(fill="x", padx=20, pady=(0,16))

  # Tema Visual
  tk.Label(settings_window, text=t("pref_theme"), font=("Arial", 11, "bold"),
           bg=p["bg"], fg=p["fg"]).pack(anchor="w", padx=20, pady=(0,4))
  theme_var = tk.StringVar(value=DEFAULT_CONFIG['theme'])
  tf = tk.Frame(settings_window, bg=p["bg"])
  tf.pack(anchor="w", padx=30, pady=(0,14))
  for label, val in [(t("pref_theme_dark"), "dark"), (t("pref_theme_light"), "light")]:
    tb.Radiobutton(tf, text=label, variable=theme_var, value=val).pack(side="left", padx=10)

  # Cor de Destaque
  tk.Label(settings_window, text=t("pref_accent"), font=("Arial", 11, "bold"),
           bg=p["bg"], fg=p["fg"]).pack(anchor="w", padx=20, pady=(0,4))
  color_var = tk.StringVar(value=DEFAULT_CONFIG['accent_color'])
  cf = tk.Frame(settings_window, bg=p["bg"])
  cf.pack(anchor="w", padx=30, pady=(0,14))
  for name, hex_val in [(t("pref_color_purple"), "#7c5cff"),
                        (t("pref_color_teal"), "#00d9a3"),
                        (t("pref_color_blue"), "#4a9eff"),
                        (t("pref_color_red"), "#e05263")]:
    tb.Radiobutton(cf, text=name, variable=color_var, value=hex_val).pack(side="left", padx=8)

  # Idioma / Language
  tk.Label(settings_window, text=t("pref_language"), font=("Arial", 11, "bold"),
           bg=p["bg"], fg=p["fg"]).pack(anchor="w", padx=20, pady=(0,4))
  lang_var = tk.StringVar(value=DEFAULT_CONFIG.get('language', 'pt_BR'))
  lf = tk.Frame(settings_window, bg=p["bg"])
  lf.pack(anchor="w", padx=30, pady=(0,20))
  for label, val in [(t("pref_lang_pt"), "pt_BR"),
                     (t("pref_lang_en"), "en_US"),
                     (t("pref_lang_es"), "es_ES")]:
    tb.Radiobutton(lf, text=label, variable=lang_var, value=val).pack(side="left", padx=6)

  def apply_and_save():
    apply_live_preferences(theme_var.get(), color_var.get(), lang_var.get())
    messagebox.showinfo(t("pref_saved_title"),
      t("pref_saved_msg"),
      parent=settings_window)
    settings_window.destroy()

  RoundedButton(settings_window, text=t("pref_btn_save"), command=apply_and_save,
                bg=p["accent"], fg="#fff", width=175, height=38).pack(pady=4)

def exit_app():
  root.quit()

# ============================================================
# LIVE PREFERENCES & THEME RELOAD
# ============================================================
lbl_header_title = None
lbl_header_mon = None
sep1 = None
sep2 = None
lbl_image_view = None
image_mode_buttons = []
btn_copy = None
btn_del = None
btn_save = None
btn_deleted = None

def rebuild_menu():
  global menubar
  menubar = tk.Menu(root)
  root.config(menu=menubar)
  m_arq = tk.Menu(menubar, tearoff=0)
  m_arq.add_command(label=t("menu_save_txt"), command=save_as_txt)
  m_arq.add_separator()
  m_arq.add_command(label=t("menu_exit"), command=exit_app)
  menubar.add_cascade(label=t("menu_file"), menu=m_arq)

  m_edit = tk.Menu(menubar, tearoff=0)
  m_edit.add_command(label=t("menu_delete"), command=delete_selected)
  m_edit.add_command(label=t("menu_deleted"), command=open_deleted_window)
  menubar.add_cascade(label=t("menu_edit"), menu=m_edit)

  view_modes = [
    ("Detalhes", t("view_details")),
    ("Icones Pequenos", t("view_small")),
    ("Icones Medios", t("view_medium")),
    ("Icones Grandes", t("view_large")),
  ]

  m_exib = tk.Menu(menubar, tearoff=0)
  for mode_key, mode_label in view_modes:
    m_exib.add_command(label=mode_label, command=lambda m=mode_key: change_view_mode(m))
  menubar.add_cascade(label=t("menu_view"), menu=m_exib)

  m_cfg = tk.Menu(menubar, tearoff=0)
  m_cfg.add_command(label=t("menu_preferences"), command=open_settings)
  menubar.add_cascade(label=t("menu_settings"), menu=m_cfg)

def apply_live_preferences(new_theme, new_accent, new_lang):
  save_config(new_theme, new_accent, new_lang)
  setup_theme()
  p = get_palette()

  root.configure(bg=p["bg"])
  rebuild_menu()

  # Cabeçalho
  if hf: hf.config(bg=p["bg"])
  if lbl_header_title: lbl_header_title.config(bg=p["bg"], fg=p["fg"])
  if lbl_header_mon: lbl_header_mon.config(text=t("monitoring"), bg=p["bg"], fg=p["fg_dim"])
  if sep1: sep1.config(bg=p["border"])

  # Abas
  if tab_bar:
    tab_bar.update_palette_and_labels(
      p, tabs=[("", t("tab_texts")), ("", t("tab_links")), ("", t("tab_images"))]
    )

  # Controles de imagem
  if frame_image_controls: frame_image_controls.config(bg=p["bg"])
  if lbl_image_view: lbl_image_view.config(text=t("view_label"), bg=p["bg"], fg=p["fg_dim"])
  view_modes = [
    ("Detalhes", t("view_details")),
    ("Icones Pequenos", t("view_small")),
    ("Icones Medios", t("view_medium")),
    ("Icones Grandes", t("view_large")),
  ]
  for btn, (mode_key, mode_label) in zip(image_mode_buttons, view_modes):
    btn.set_text(mode_label)
    btn.set_colors(bg=p["ter_bg"], fg=p["fg"], hover_bg=p["accent"], active_bg=p["accent"], parent_bg=p["bg"])

  # Área de conteúdo
  if content_host: content_host.config(bg=p["bg"])
  if frame_text: frame_text.config(bg=p["sec_bg"])
  if custom_list_text: custom_list_text.update_palette(p)
  if frame_link: frame_link.config(bg=p["sec_bg"])
  if custom_list_link: custom_list_link.update_palette(p)

  # Imagens
  if frame_image: frame_image.config(bg=p["sec_bg"])
  if images_canvas: images_canvas.config(bg=p["sec_bg"])
  if images_inner_frame: images_inner_frame.config(bg=p["sec_bg"])
  update_images_view()

  # Separador inferior e botões
  if sep2: sep2.config(bg=p["border"])
  if bf: bf.config(bg=p["bg"])

  if btn_copy:
    btn_copy.set_text(t("btn_copy"))
    btn_copy.set_colors(bg=p["accent"], fg="#fff", parent_bg=p["bg"])

  if btn_del:
    btn_del.set_text(t("btn_delete"))
    btn_del.set_colors(bg=p["danger"], fg="#fff", parent_bg=p["bg"])

  if btn_save:
    btn_save.set_text(t("btn_save_img") if current_tab_index == 2 else t("btn_save_txt"))
    btn_save.set_colors(bg=p["success"], fg="#fff", parent_bg=p["bg"])

  if btn_deleted:
    btn_deleted.set_text(t("btn_deleted"))
    btn_deleted.set_colors(bg=p["bg"], fg=p["fg"], hover_bg=p["ter_bg"], active_bg=p["sec_bg"],
                           border_color=p["border"], border_width=1, parent_bg=p["bg"])

# ============================================================
# THEME SETUP
# ============================================================
def setup_theme():
  style = tb.Style()
  p = get_palette()
  is_dark = p["is_dark"]
  try:
    ct = {
      "primary": p["accent"], "secondary": p["sec_bg"],
      "success": p["success"], "info": "#4a9eff",
      "warning": "#ffb84d", "danger": p["danger"],
      "light": "#f8f9fa", "dark": "#17172a",
      "bg": p["bg"], "fg": p["fg"],
      "selectbg": p["accent"], "selectfg": "#ffffff",
      "border": p["border"], "inputfg": p["fg"],
      "inputbg": p["sec_bg"], "active": p["ter_bg"],
    }
    tn = "cclip_dark" if is_dark else "cclip_light"
    td = {"themes": [{tn: {"type": "dark" if is_dark else "light", "colors": ct}}]}
    with open("custom_themes.json", "w", encoding="utf-8") as f: json.dump(td, f)
    style.load_user_themes("custom_themes.json")
    style.theme_use(tn)
  except Exception:
    style.theme_use("darkly" if is_dark else "cosmo")

  # Fix 1: Scrollbar — paleta escura, sem seta colorida do sistema
  style.configure("Vertical.TScrollbar",
    background=p["ter_bg"],
    troughcolor=p["bg"],
    arrowcolor=p["bg"],
    bordercolor=p["bg"],
    lightcolor=p["bg"],
    darkcolor=p["bg"],
    borderwidth=0,
    relief="flat",
    width=8,
  )
  style.map("Vertical.TScrollbar",
    background=[("active", p["border"]), ("disabled", p["sec_bg"])],
    arrowcolor=[("active", p["bg"]), ("disabled", p["bg"])],
  )
  style.configure("Horizontal.TScrollbar",
    background=p["ter_bg"], troughcolor=p["bg"],
    arrowcolor=p["bg"], borderwidth=0, relief="flat", width=8,
  )
  style.map("Horizontal.TScrollbar",
    background=[("active", p["border"]), ("disabled", p["sec_bg"])],
  )

# ============================================================
# ROOT SETUP
# ============================================================
root = tb.Window(title="Clipboard History Manager")
root.geometry("780x640")
setup_theme()
p = get_palette()
root.configure(bg=p["bg"])

# --- Menu Bar ---
rebuild_menu()

# --- Header ---
hf = tk.Frame(root, bg=p["bg"])
hf.pack(fill="x", padx=24, pady=(16, 0))
lbl_header_title = tk.Label(hf, text="Clipboard History Manager",
         font=("Arial", 18, "bold"), bg=p["bg"], fg=p["fg"])
lbl_header_title.pack(side="left")
lbl_header_mon = tk.Label(hf, text=t("monitoring"), font=("Arial", 9),
         bg=p["bg"], fg=p["fg_dim"])
lbl_header_mon.pack(side="left", padx=(10, 0), pady=(6, 0))

# --- Separador ---
sep1 = tk.Frame(root, bg=p["border"], height=1)
sep1.pack(fill="x", padx=24, pady=(10, 0))

# --- Tab Bar ---
# Fix 2: Removidos os ícones □ que eram confundidos com indicador de foco
tab_bar = CustomTabBar(
  root,
  tabs=[("", t("tab_texts")), ("", t("tab_links")), ("", t("tab_images"))],
  on_change=on_tab_change,
  palette=p,
)
tab_bar.pack(fill="x", padx=24, pady=(10, 0))

# --- Image Controls (hidden by default) ---
frame_image_controls = tk.Frame(root, bg=p["bg"])
lbl_image_view = tk.Label(frame_image_controls, text=t("view_label"), font=("Arial", 9),
         bg=p["bg"], fg=p["fg_dim"])
lbl_image_view.pack(side="left", padx=(0,6))
view_modes = [
  ("Detalhes", t("view_details")),
  ("Icones Pequenos", t("view_small")),
  ("Icones Medios", t("view_medium")),
  ("Icones Grandes", t("view_large")),
]
image_mode_buttons = []
for mode_key, mode_label in view_modes:
  btn_m = RoundedButton(
    frame_image_controls, text=mode_label,
    command=lambda m=mode_key: change_view_mode(m),
    bg=p["ter_bg"], fg=p["fg"],
    hover_bg=p["accent"], active_bg=p["accent"],
    radius=10, width=120, height=28, font=("Arial", 9),
  )
  btn_m.pack(side="left", padx=4)
  image_mode_buttons.append(btn_m)

# --- Tab Content Area ---
content_host = tk.Frame(root, bg=p["bg"])
content_host.pack(expand=True, fill="both", padx=20, pady=(6, 0))

# Tab 0: Textos
frame_text = tk.Frame(content_host, bg=p["sec_bg"])
custom_list_text = CustomList(
  frame_text, palette=p,
  on_select=lambda idx, text: open_edit_window(idx, text, 'text')
)
custom_list_text.pack(expand=True, fill="both", padx=2, pady=2)

# Tab 1: Links
frame_link = tk.Frame(content_host, bg=p["sec_bg"])
custom_list_link = CustomList(
  frame_link, palette=p,
  on_select=lambda idx, text: open_edit_window(idx, text, 'link')
)
custom_list_link.pack(expand=True, fill="both", padx=2, pady=2)

# Tab 2: Imagens
frame_image = tk.Frame(content_host, bg=p["sec_bg"])
images_canvas = tk.Canvas(frame_image, bg=p["sec_bg"], bd=0, highlightthickness=0)
images_canvas.pack(side="left", expand=True, fill="both", padx=12, pady=12)
scrollbar_img = ttk.Scrollbar(frame_image, orient="vertical", command=images_canvas.yview)
scrollbar_img.pack(side="right", fill="y", pady=12)
images_canvas.configure(yscrollcommand=scrollbar_img.set)
images_inner_frame = tk.Frame(images_canvas, bg=p["sec_bg"])
images_canvas.create_window((0, 0), window=images_inner_frame, anchor="nw")
images_inner_frame.bind("<Configure>",
  lambda e: images_canvas.configure(scrollregion=images_canvas.bbox("all")))

tab_frames = [frame_text, frame_link, frame_image]

# Show first tab
frame_text.pack(expand=True, fill="both")

# --- Bottom Separator ---
sep2 = tk.Frame(root, bg=p["border"], height=1)
sep2.pack(fill="x", padx=24, pady=(8, 0))

# --- Bottom Buttons ---
bf = tk.Frame(root, bg=p["bg"])
bf.pack(pady=18)

btn_copy = RoundedButton(bf, text=t("btn_copy"), command=copy_selected,
              bg=p["accent"], fg="#fff",
              radius=16, width=160, height=42)
btn_copy.grid(row=0, column=0, padx=7)

btn_del = RoundedButton(bf, text=t("btn_delete"), command=delete_selected,
              bg=p["danger"], fg="#fff",
              radius=16, width=125, height=42)
btn_del.grid(row=0, column=1, padx=7)

btn_save = RoundedButton(bf, text=t("btn_save_txt"), command=save_as_file,
              bg=p["success"], fg="#fff",
              radius=16, width=145, height=42)
btn_save.grid(row=0, column=2, padx=7)

btn_deleted = RoundedButton(bf, text=t("btn_deleted"), command=open_deleted_window,
              bg=p["bg"], fg=p["fg"],
              hover_bg=p["ter_bg"], active_bg=p["sec_bg"],
              border_color=p["border"], border_width=1,
              radius=16, width=135, height=42)
btn_deleted.grid(row=0, column=3, padx=7)

if __name__ == "__main__":
  save_clipboard()
  root.mainloop()
