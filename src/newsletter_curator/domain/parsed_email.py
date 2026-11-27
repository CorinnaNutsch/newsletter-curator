from dataclasses import dataclass


@dataclass
class NewsletterArticle:
    title: str
    url: str
    sponsored: bool
    text: str


@dataclass
class NewsletterIssue:
    source: str
    date: str
    articles: list[NewsletterArticle]
