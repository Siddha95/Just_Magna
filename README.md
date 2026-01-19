# JustMagna 🍽️

Un sistema completo di gestione ristorante e e-commerce per la ristorazione, costruito con Django.

## 📋 Descrizione

JustMagna è un'applicazione web completa che combina funzionalità di catalogo menu, e-commerce, e gestione della relazione con i clienti (CRM) per ristoranti. Il sistema permette di gestire piatti, ordini, carrelli della spesa, e feedback dei clienti in un'unica piattaforma integrata.

## ✨ Funzionalità Principali

### 🍕 Catalog (Catalogo)

- **Gestione piatti**: Creazione e modifica di piatti con informazioni dettagliate
- **Portate**: Organizzazione dei piatti per portata (antipasti, primi, secondi, ecc.)
- **Ingredienti**: Database degli ingredienti con proprietà dietetiche
- **Filtri dietetici**: Supporto per piatti vegetariani, vegani e senza glutine
- **Immagini**: Upload e gestione immagini dei piatti
- **Prezzi**: Gestione prezzi e descrizioni

### 🛒 E-commerce

- **Carrello**: Sistema completo di gestione carrello della spesa
- **Ordini**: Gestione ordini dei clienti
- **Voucher**: Sistema di sconti e voucher con date di validità
- **Indirizzi**: Gestione indirizzi di consegna
- **Fatture**: Sistema di fatturazione integrato
- **Calcolo totali**: Calcolo automatico del totale carrello

### 👥 CRM (Customer Relationship Management)

- **Survey**: Sistema di sondaggi per raccogliere feedback
- **Rating**: Valutazioni dei piatti e delle portate (scala 1-49)
- **Piatto preferito**: Gli utenti possono indicare il piatto preferito
- **Feedback testuale**: Commenti e suggerimenti dei clienti
- **Analisi dati**: Raccolta dati per migliorare il servizio

### 🔐 Accounts (Gestione Utenti)

- Sistema di autenticazione e registrazione utenti
- Gestione profili
- API per operazioni utente

## 🛠️ Tecnologie Utilizzate

- **Framework**: Django 5.1.2
- **Database**: SQLite3 (sviluppo)
- **Frontend**: Bootstrap 5 con Crispy Forms
- **API**: Django REST Framework
- **Autenticazione API**: Token-based authentication
- **Template Engine**: Django Templates
- **Storage Media**: Sistema di upload file Django

## 📦 Struttura del Progetto

```
justmagna/
├── accounts/          # App gestione utenti e autenticazione
├── catalog/           # App catalogo piatti e ingredienti
├── crm/              # App CRM (survey e rating)
├── ecommerce/        # App e-commerce (carrello, ordini, voucher)
├── justmagna/        # Configurazione principale del progetto
├── templates/        # Template HTML
├── static/           # File statici (CSS, immagini)
├── media/            # File caricati dagli utenti
└── manage.py         # Script di gestione Django
```

## 🚀 Installazione

### Prerequisiti

- Python 3.8+
- pip (gestore pacchetti Python)

### Passaggi di Installazione

1. **Clone o scarica il progetto**

```bash
cd /path/to/justmagna
```

2. **Crea un ambiente virtuale**

```bash
python -m venv myvenv
```

3. **Attiva l'ambiente virtuale**

**macOS/Linux:**

```bash
source myvenv/bin/activate
```

**Windows:**

```bash
myvenv\Scripts\activate
```

4. **Installa le dipendenze**

```bash
pip install -r requirements.txt
```

5. **Esegui le migrazioni del database**

```bash
python manage.py migrate
```

6. **Crea un superutente (amministratore)**

```bash
python manage.py createsuperuser
```

7. **Avvia il server di sviluppo**

```bash
python manage.py runserver
```

8. **Accedi all'applicazione**

- Sito web: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## 📱 API Endpoints

Il progetto include API RESTful per tutte le app principali:

- `/api/accounts/` - Gestione utenti
- `/api/catalog/` - Piatti, portate e ingredienti
- `/api/crm/` - Survey e rating
- `/api/ecommerce/` - Carrello, ordini e voucher

**Autenticazione**: Token-based (REST Framework)

## 🗄️ Modelli del Database

### Catalog

- **Course**: Portate (antipasti, primi, secondi, ecc.)
- **Dish**: Piatti con proprietà dietetiche, prezzo e immagine
- **Ingredient**: Ingredienti con proprietà dietetiche

### E-commerce

- **Cart**: Carrello utente
- **Cart_dish**: Articoli nel carrello con quantità
- **Voucher**: Buoni sconto con validità temporale
- **Order**: Ordini (in sviluppo)
- **Address**: Indirizzi di consegna (in sviluppo)
- **Invoice**: Fatture (in sviluppo)

### CRM

- **Survey**: Sondaggio utente
- **Rating**: Valutazione per portata con voto e piatto preferito

## ⚙️ Configurazione

### Impostazioni Principali (settings.py)

- **Lingua**: Italiano (`it`)
- **Timezone**: Europe/Berlin
- **Debug Mode**: Attivato (da disattivare in produzione)
- **Static Files**: `/static/`
- **Media Files**: `/media/`

### ⚠️ Note sulla Sicurezza

**Prima del deployment in produzione:**

1. Cambia `SECRET_KEY` in `settings.py`
2. Imposta `DEBUG = False`
3. Configura `ALLOWED_HOSTS` con i domini corretti
4. Usa un database di produzione (PostgreSQL consigliato)
5. Configura HTTPS
6. Implementa backup regolari del database

## 🎨 Frontend

Il progetto utilizza:

- **Bootstrap 5** per il responsive design
- **Crispy Forms** per form eleganti
- **Template personalizzati** in `/templates/`
- **CSS custom** in `/static/css/`

## 🔄 Context Processors Personalizzati

- `crm.context_processors.courses_list` - Lista portate disponibile in tutti i template
- `ecommerce.context_processors.cart_item_count` - Contatore articoli carrello

## 📝 Comandi Utili

```bash
# Creare migrazioni dopo modifiche ai modelli
python manage.py makemigrations

# Applicare migrazioni
python manage.py migrate

# Creare superutente
python manage.py createsuperuser

# Raccogliere file statici
python manage.py collectstatic

# Avviare shell Django
python manage.py shell

# Eseguire test
python manage.py test
```

## 🤝 Contribuire

Per contribuire al progetto:

1. Crea un branch per la tua feature
2. Implementa le modifiche
3. Testa accuratamente
4. Crea una pull request

## 📄 Licenza

Questo progetto è distribuito sotto licenza privata. Tutti i diritti riservati.

## 📧 Contatti

Per domande o supporto, contattare il team di sviluppo.

## 🗺️ Roadmap

### Features in Sviluppo

- [ ] Completamento modelli Order, Address, Invoice
- [ ] Sistema di pagamento integrato
- [ ] Notifiche email per ordini
- [ ] Dashboard analytics per amministratori
- [ ] App mobile
- [ ] Sistema di prenotazione tavoli
- [ ] Menu digitale con QR code
- [ ] Integrazione con sistemi di consegna

---

**Versione**: 1.0.0  
**Framework**: Django 5.1.2  
**Python**: 3.8+  
**Ultimo aggiornamento**: Gennaio 2026
