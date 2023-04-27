import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import slugify from 'slugify';

const AddPost = () => {
  const navigate = useNavigate();
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [category, setCategory] = useState("");
  const [slug, setSlug] = useState("11");
  const [author, setAuthor] = useState("");
  const [image, setImage] = useState(null);
  const newSlug = slugify(title, { lower: true, strict: true });

  console.log(slug);

  useEffect(() => {
    setSlug(newSlug)
  }, [title, newSlug]);
  
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Создаем объект FormData для отправки данных на сервер
    const formData = new FormData();
    formData.append("image", image);
    formData.append("title", title);
    formData.append("content", content);
    formData.append("slug", slug);
    formData.append("category_id", category);
    formData.append("author_id", author);

    try {
      // Отправляем данные на сервер с помощью axios
      const response = await axios.post("http://127.0.0.1:8000/api/v1/news/", formData);
      console.log(response.data.results);
      navigate('/');
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form style={{ padding: '50px 400px' }} onSubmit={handleSubmit}>
      <div>
        <label htmlFor="title">Заголовок:</label>
        <input className="form-control required" placeholder="Title" type="text" id="title" value={title} onChange={(e) => setTitle(e.target.value)} />
      </div>
      <br />
      <div>
        <label htmlFor="content">Текст:</label>
        <textarea className="form-control required" placeholder="Content" id="content" value={content} onChange={(e) => setContent(e.target.value)} />
      </div>
      <br />
      <div>
        <label htmlFor="image">Изображение:</label> <br />
        <input type="file" id="image" onChange={(e) => setImage(e.target.files[0])} />
      </div>
      <br />
      <div>
        <label htmlFor="title">Категория:</label>
        <select value={category} name="catselect" onChange={(e) => setCategory(e.target.value)} class="form-control valid" aria-invalid="false">
            <option value="" disabled="" selected="">Select a Category</option>
            <option value="1">Action/RPG</option>
            <option value="2">Strategy</option>
            <option value="3">Shooter</option>
            <option value="4">Indie</option>
            <option value="5">Other</option>
        </select>
      </div>
      <br />
      <div>
        <label htmlFor="title">Автор:</label>
        <select value={author} name="authselect" onChange={(e) => setAuthor(e.target.value)} class="form-control valid" aria-invalid="false">
            <option value="" disabled="" selected="">Select an Author</option>
            <option value="1">CaleAnto</option>
            <option value="2">FlazyFlad</option>
        </select>
      </div>
      <br />
      <button className="nk-btn nk-btn-rounded nk-btn-color-dark-3" type="submit">Добавить пост</button>
    </form>
  );
};

export default AddPost;
