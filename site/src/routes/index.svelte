<script context="module">
	import { assets } from "$app/paths";

	export async function load({ page, fetch, session, context }) {
		const res = await fetch(`${assets}/ingredients.json`);
		const { types, ...ingredients } = await res.json();

		return { props: { types, ingredients } };
	}
</script>

<script>
	import { onMount } from "svelte";
	import Layer from "$lib/Layer.svelte";
	import { layers } from "$lib/stores.js";

	export let ingredients = {};
	export let types = {};

	onMount(() => {
		layers.restore();
		layers.subscribe(value => {
			window.layers = value;
		});
	});
</script>

<svelte:head>
	<title>Salad Spinner</title>
</svelte:head>

<header>
	<h1>Salad spinner</h1>
	<p class="lead">Let's have a summer of salad.</p>
</header>

<div class="add">
	<h2>Add something</h2>
	<ul class="types nav nav-pills nav-fill">
		{#each Object.entries(types) as [id, type]}
			<li class="nav-item">
				<button class="btn btn-light {id}" on:click={e => layers.add(id)}
					>{type.name}</button
				>
			</li>
		{/each}
	</ul>
</div>

<form class="layers">
	<h2>Ingredients</h2>
	{#each $layers as layer, index (layer)}
		<Layer
			id={layer.type}
			name={types[layer.type].name}
			ingredients={ingredients[layer.type]}
			{index}
		/>
	{/each}

	<div class="submit">
		<input class="btn btn-primary" type="submit" value="Save this salad" />
	</div>
</form>

<style>
	.types {
		margin-bottom: 1.5em;
	}

	.types button {
		margin-bottom: 0.5em;
	}
</style>
