import api
import docs
import justpy as jp

jp.Route("/api", api.Api.serve)
jp.Route("/", docs.Docs.serve)
jp.justpy()
