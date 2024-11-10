import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { VitePWA } from "vite-plugin-pwa";
import frappeui from "frappe-ui/vite";
import path from "path";
import fs from "fs";

export default defineConfig({
	server: {
		port: 8080,
		proxy: getProxyOptions(),
	},
	plugins: [
		vue(),
		frappeui(),
		VitePWA({
			registerType: "autoUpdate",
			strategies: "injectManifest",
			injectRegister: null,
			devOptions: {
				enabled: true,
			},
			manifest: {
				display: "standalone",
				name: "Pwit App",
				short_name: "Pwit",
				start_url: "/pwit",
				description: "An app for Pwit operations",
				theme_color: "#ffffff",
			
			},
		}),
	],
	resolve: {
		alias: {
			"@": path.resolve(__dirname, "src"),
		},
	},
	build: {
		outDir: "../pwit/public/frontend", // Adjusted for pwit
		emptyOutDir: true,
		target: "es2015",
		commonjsOptions: {
			include: [/tailwind.config.js/, /node_modules/],
		},
		sourcemap: true,
		rollupOptions: {
			output: {
				manualChunks: {
					"frappe-ui": ["frappe-ui"],
				},
			},
		},
	},
	optimizeDeps: {
		include: [
			"frappe-ui > feather-icons",
			"showdown",
			"tailwind.config.js",
			"engine.io-client",
		],
	},
});

// Helper function for proxy configuration
function getProxyOptions() {
	const config = getCommonSiteConfig();
	const webserverPort = config ? config.webserver_port : 8000;

	if (!config) {
		console.log("No common_site_config.json found, using default port 8000");
	}

	return {
		"^/(app|login|api|assets|files|private)": {
			target: `http://127.0.0.1:${webserverPort}`,
			ws: true,
			router: req => {
				const siteName = req.headers.host.split(":")[0];
				console.log(`Proxying ${req.url} to ${siteName}:${webserverPort}`);
				return `http://${siteName}:${webserverPort}`;
			},
		},
	};
}

// Helper function to locate and read common_site_config.json
function getCommonSiteConfig() {
	let currentDir = path.resolve(".");

	// Traverse up the directory tree until we find `frappe-bench/sites`
	while (currentDir !== "/") {
		if (
			fs.existsSync(path.join(currentDir, "sites")) &&
			fs.existsSync(path.join(currentDir, "apps"))
		) {
			const configPath = path.join(currentDir, "sites", "common_site_config.json");
			if (fs.existsSync(configPath)) {
				return JSON.parse(fs.readFileSync(configPath, 'utf-8'));
			}
			return null;
		}
		currentDir = path.resolve(currentDir, "..");
	}
	return null;
}
