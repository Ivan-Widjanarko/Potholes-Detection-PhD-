package id.develo.capstoneproject.ui.authentication

import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.viewModels
import com.google.android.material.snackbar.Snackbar
import id.develo.capstoneproject.databinding.FragmentRegisterBinding


class RegisterFragment : Fragment() {

    private var _binding: FragmentRegisterBinding? = null
    private val binding get() = _binding!!

    private val registerViewModel: RegisterViewModel by viewModels()

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        _binding = FragmentRegisterBinding.inflate(inflater, container, false)
        val view = binding.root
        return view
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        setProgressBar()
        launchSnackBar()

        binding.btnRegister.setOnClickListener {
            register()
            moveToLoginIfSuccess()
        }

        binding.tvSignin.setOnClickListener {
            // Back to Login Page
            parentFragmentManager.popBackStack()
        }
    }

    fun register() {
        if (binding.tfEmail.editText?.text!!.isEmpty()) {
            binding.tfEmail.error = "This field is required!"
        } else binding.tfEmail.error = null
        if (binding.tfPassword.editText?.text!!.isEmpty()) {
            binding.tfPassword.error = "This field is required!"
        } else binding.tfPassword.error = null
        if (binding.tfDeviceId.editText?.text!!.isEmpty()) {
            binding.tfDeviceId.error = "This field is required!"
        } else binding.tfDeviceId.error = null

        val inputEmail = binding.tfEmail.editText?.text.toString()
        val inputPassword = binding.tfPassword.editText?.text.toString()
        val inputDeviceId = binding.tfDeviceId.editText?.text.toString()

//        Log.d("TEST em", inputEmail)
//        Log.d("TEST pa", inputPassword)
//        Log.d("TEST id", inputDeviceId)

        registerViewModel.registerUser(
            inputEmail,
            inputPassword,
            inputDeviceId.toInt()
        )
    }

    fun launchSnackBar() {
        registerViewModel.snackbarText.observe(requireActivity(), {
            it.getContentIfNotHandled()?.let { snackbarText ->
                Snackbar.make(
                    requireActivity().window.decorView.rootView,
                    snackbarText,
                    Snackbar.LENGTH_LONG
                ).show()
            }
        })
    }

    fun moveToLoginIfSuccess() {
        registerViewModel.isSuccess.observe(requireActivity(), {
            if (it) parentFragmentManager.popBackStack()
        })
    }

    fun setProgressBar() {
        registerViewModel.isLoading.observe(requireActivity(), {
            binding.progressBar.visibility = if (it) View.VISIBLE else View.GONE
        })
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }


}