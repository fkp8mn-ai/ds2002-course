use bookstore

db.authors.insertOne({
  name: "Jane Austen",
  nationality: "British",
  bio: {
    short: "English novelist known for novels about the British landed gentry.",
    long: "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century."
  }
})

db.authors.updateOne(
  { name: "Jane Austen" },
  { $set: { birthday: "1775-12-16" } }
)

db.authors.insertMany([
{
  name: "Mark Twain",
  nationality: "American",
  birthday: "1835-11-30",
  bio: {
    short: "American writer and humorist.",
    long: "Mark Twain was an American writer best known for The Adventures of Tom Sawyer and Adventures of Huckleberry Finn."
  }
},
{
  name: "Charles Dickens",
  nationality: "British",
  birthday: "1812-02-07",
  bio: {
    short: "English novelist of the Victorian era.",
    long: "Charles Dickens created some of the world's best known fictional characters."
  }
},
{
  name: "Gabriel Garcia Marquez",
  nationality: "Colombian",
  birthday: "1927-03-06",
  bio: {
    short: "Colombian novelist and Nobel Prize winner.",
    long: "Gabriel Garcia Marquez was a key figure in magical realism."
  }
},
{
  name: "Haruki Murakami",
  nationality: "Japanese",
  birthday: "1949-01-12",
  bio: {
    short: "Japanese novelist blending surrealism and realism.",
    long: "Haruki Murakami is known for works like Norwegian Wood and Kafka on the Shore."
  }
}
])

db.authors.countDocuments()

db.authors.find({ nationality: "British" }).sort({ name: 1 })
