<template class="container">
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-md-6 shadow p-4 rounded">
                <h2 class="text-center mb-4">Generate Your QR Code</h2>
                <form @submit.prevent>
                    <div class="mb-3">
                        <label for="text" class="form-label">Enter Text:</label>
                        <input type="text" v-model="text" class="form-control" id="text" placeholder="Enter text to encode"
                            required>
                    </div>
                    <div class="mb-3">
                        <label for="colorPicker" class="form-label">Choose Color:</label>
                        <input type="color" v-model="selectedColor" class="form-control form-control-color"
                            id="colourPicker" title="Choose your color">
                    </div>
                    <button @click="submitForm()" type="button" id="generateBtn" class="btn btn-primary w-100">
                        Generate QRCode
                    </button>
                </form>


                <div class="mt-4 text-center">
                    <div class="d-flex justify-content-center align-items-center" id="qrCodeContainer">
                        <img :src="img" v-if="img" alt="QR Code" />
                    </div>
                    <div class="mt-2">
                        <button @click="downloadQrCode()" id="downloadBtn" class="btn btn-outline-primary">Download QR
                            Code</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import { ref } from 'vue';
const apiUrl = `http://localhost:8091/api/generate-qrcode/`;
export default {
    setup() {
        const formData = {
            text: ref(''),
            img: ref(''),
            selectedColor: ref(''),
        };

        function downloadQrCode() {
            if (!formData.img.value) {
                return;
            }

            const a = document.createElement('a');
            a.href = formData.img.value;
            const filename = `qr-code-${formData.text.value}-${formData.selectedColor.value}.png`;
            a.download = filename;

            a.click();
            a.remove();
        }

        async function submitForm() {
            if (formData.text.value !== '') {

                try {
                    const response = await fetch(`${apiUrl}?colour=${encodeURIComponent(formData.selectedColor.value)}`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            text: formData.text.value,
                        }),
                    });

                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }

                    const blob = await response.blob();
                    const imageURL = URL.createObjectURL(blob);
                    formData.img.value = imageURL;
                } catch (error) {
                    console.error('Error:', error);
                }
            }
        }

        return {
            ...formData,
            submitForm,
            downloadQrCode,
        };
    },
};

</script>