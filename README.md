body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f5f7fb;
  color: #1f2937;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 24px;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 22px;
}

.search {
  display: flex;
  gap: 8px;
}

.search input {
  width: 320px;
  padding: 10px 12px;
  border-radius: 8px;
  border: 1px solid #dfe4ec;
}

.search button {
  padding: 10px 16px;
  border: none;
  border-radius: 8px;
  background: #2563eb;
  color: white;
  cursor: pointer;
}

.stats {
  display: grid;
  grid-template-columns: repeat(3, minmax(180px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 18px;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.05);
}

.stat-card span {
  color: #64748b;
  display: block;
  margin-bottom: 8px;
}

.stat-card strong {
  font-size: 28px;
}

.posts {
  display: grid;
  gap: 16px;
}

.post-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.05);
  padding: 18px;
}

.meta-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.caption {
  line-height: 1.6;
  margin: 12px 0;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 10px;
}

.tags span {
  background: #dbeafe;
  color: #1d4ed8;
  font-size: 12px;
  padding: 4px 8px;
  border-radius: 999px;
}

.details, .footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #475569;
  font-size: 13px;
}

.footer {
  margin-top: 12px;
}

a {
  color: #2563eb;
  text-decoration: none;
}
