# personal library management system

import streamlit as st

# Function to set background
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover; 
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

bg_image = "https://media.istockphoto.com/id/1217642566/vector/library-vector-background-pile-books-open-textbook-cup-of-coffee-and-plant-locate-on-wooden.jpg?s=612x612&w=0&k=20&c=kkETV6-jDSPqzBHlVoiunz8o8Fn378ozoNTBo0XHNSQ="
set_background(bg_image)

# Book class
class Book:
    def __init__(self, title, author, isbn, description, status="Unread"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status
        self.description = description

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - ({self.description}) - {self.status}"

# Initialize session state for books
if "books" not in st.session_state:
    st.session_state["books"] = []

st.sidebar.header("📖 Library Actions")
option = st.sidebar.selectbox("Select an action", ["Add Book", "Update Book Status", "Remove Book", "View Books"])

# Add Book
if option == "Add Book":
    st.subheader("📗 Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    isbn = st.text_input("ISBN")
    description = st.text_input("Description")
    if st.button("Add Book"):
        if title and author and isbn:
            st.session_state["books"].append(Book(title, author, isbn, description))
            st.success(f"Book '{title}' added successfully!")
        else:
            st.warning("Please fill in all fields.")

# Update Book Status
elif option == "Update Book Status":
    st.subheader("✅ Update Book Status")
    
    if st.session_state["books"]:
        book_titles = [book.title for book in st.session_state["books"]]
        selected_book = st.selectbox("Select a book to update", book_titles)
        new_status = st.selectbox("New Status", ["Unread", "Reading", "Read"])

        if st.button("Update Status"):
            for book in st.session_state["books"]:
                if book.title == selected_book:
                    book.status = new_status
                    st.success(f"Status updated to '{new_status}' for '{selected_book}'!")
                    break
    else:
        st.warning("No books available to update.")

# Remove Book
elif option == "Remove Book":
    st.subheader("🗑️ Remove a Book")

    if st.session_state["books"]:
        book_titles = [book.title for book in st.session_state["books"]]
        book_to_remove = st.selectbox("Select a book to remove", book_titles)

        if st.button("Delete Book"):
            st.session_state["books"] = [book for book in st.session_state["books"] if book.title != book_to_remove]
            st.success(f"'{book_to_remove}' has been removed!")
            st.experimental_rerun()
    else:
        st.warning("No books available to remove.")

# View Books
elif option == "View Books":
    st.subheader("📚 Available Books")
    if st.session_state["books"]:
        for book in st.session_state["books"]:
            st.write(f"📖 {book}")
    else:
        st.info("No books in the library yet.")
                
