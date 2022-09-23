from app.extensions import db

# Tabela de associacao de autor com arquivo
associationAuthorFile = db.Table("authorship", db.Model.metadata,
                                    db.Column("author_id", db.Integer, db.ForeignKey("author.id")),
                                    db.Column("file_id", db.Integer, db.ForeignKey("file.id")))

# Tabela de associacao de tag com arquivo
associationTagFile = db.Table("file_tag", db.Model.metadata,
                                    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
                                    db.Column("file_id", db.Integer, db.ForeignKey("file.id")))