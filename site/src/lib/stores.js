import { writable } from "svelte/store";

function createLayerStore() {
	const { set, subscribe, update } = writable([]);

	return {
		set,
		subscribe,
		add(type) {
			update(layers => [{ type, ingredient: null }, ...layers]);
		},
		remove(index) {
			update(layers => layers.filter((l, i) => i !== index));
		},
		restore() {
			const key = "saladspinner.layers";
			const saved = JSON.parse(localStorage.getItem(key)) || [];

			set(saved);

			subscribe(layers => {
				localStorage.setItem(key, JSON.stringify(layers));
			});
		},
	};
}

export const layers = createLayerStore();
