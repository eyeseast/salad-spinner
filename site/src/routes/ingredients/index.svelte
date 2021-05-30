<script context="module">
	import { assets } from "$app/paths";

	export async function load({ page, fetch, session, context }) {
		const res = await fetch(`${assets}/ingredients.json`);
		const { types, ...ingredients } = await res.json();

		return { props: { types, ingredients } };
	}
</script>

<script>
	export let ingredients = {};
	export let types = {};
</script>

<h1>Ingredients</h1>

<ul class="types">
	{#each Object.values(types) as type}
		<li>{type.name}</li>
	{/each}
</ul>

<ul class="ingredients">
	{#each Object.values(ingredients) as group}
		{#each group as ingredient}
			<li>{ingredient.name}</li>
		{/each}
	{/each}
</ul>
