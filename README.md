# Salad spinner

Let's make friends with salad.

## Ingredients

A salad ingredient looks like this:

```json
{
	"id": "romaine-lettuce",
	"name": "Romaine lettuce",
	"type": "greens"
}
```

That's defined in `ingredients/greens.yml`, along with other basics:

```yml
name: Greens

ingredients:
  - Arugula
  - Baby spinach
  - Iceberg Lettuce
  - Romaine Lettuce
```

It's just one thing, so all we need is a name. For something more complicated, we can add more detail:

```yml
name: Grains

ingredients:
  - name: Barley
    id: barley
    allergies: [gluten]
  - Brown rice
  - name: Bulgar wheat
    allergies: [gluten]
  - name: Farro
    allergies: [gluten]
  - Quinoa
  - Wild rice
```

Some grains need to mark allergy information (gluten, in this case) so I'm using objects instead of strings. I'm also mixing in the simpler style, because quinoa is just quinoa. The `id` field is totally optional here but included as an example.
