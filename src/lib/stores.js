import { writable } from 'svelte/store';

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
		}
	};
}

export const layers = createLayerStore();
