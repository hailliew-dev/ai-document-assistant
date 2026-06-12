import styles from "./page.module.css";

export default function Home() {
  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <div className={styles.intro}>
          <h1 className={styles.title}>AI Document Assistant</h1>
          <button type="button">Upload</button>
        </div>
      </main>
    </div>
  );
}
